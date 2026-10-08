#!/usr/bin/env python3
# Copyright (c) 2026 Juan-Antonio Søren Espinoza Pedersen
# SPDX-License-Identifier: MIT
# License text: tools/LICENSE (scoped to this validator)
"""Offline consistency checks for the Phase 1 documentation package.
Not a legal review or comprehensive security audit.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import argparse
import struct
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LICENSE_SHA256 = 'ffcca38841adb694b6f380647e15f17c446a4d1656fed51a1e2041d064c94cc8'
CC_SHA256 = '41003d4a74749c0220e33dd415042164b5a1093ed401f36277234f772d22d3d0'
MIT_SHA256 = '50657c05f52cf17ff0512ea897e52dffc728018247fdb851af0f06e41c8ca66f'
OWNER = 'Juan-Antonio Søren Espinoza Pedersen'
PRIVATE_REPORTS = ('publication/phase-1-review.md', 'publication/phase-1b-review.md')
REQUIRED = [
    'README.md', 'COPYRIGHT.md', 'LICENSING.md', 'COMMERCIAL_LICENSING.md',
    'TRADEMARKS.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'SECURITY.md',
    'GOVERNANCE.md', 'ROADMAP.md', 'licenses/README.md',
    'licenses/PolyForm-Noncommercial-1.0.0.txt',
    'licenses/DOCUMENTATION_LICENSE_REVIEW.md', 'docs/README.md',
    'docs/mission.md', 'docs/open-development-principles.md',
    'docs/technology-overview.md', 'docs/commercial-model.md',
    'docs/development-status.md', 'architecture/README.md',
    'architecture/platform-overview.md', 'architecture/embedded-control.md',
    'architecture/wireless-connectivity.md', 'architecture/telemetry-and-data.md',
    'architecture/hardware-abstraction.md', 'products/README.md',
    'products/lamp.md', 'products/motor-control.md', 'products/wireless-probe.md',
    'products/gateway.md', 'products/remote-controller.md', 'repositories/README.md',
    'repositories/repository-registry.md', 'repositories/naming-conventions.md',
    'repositories/publication-policy.md', 'provenance/README.md',
    'provenance/development-history.md', 'provenance/provenance-policy.md',
    'provenance/release-evidence.md', 'templates/firmware-readme.md',
    'templates/copyright-notice.md', 'templates/commercial-licensing.md',
    'templates/third-party-notices.md', 'templates/development-history.md',
    'templates/organization-profile-readme.md', 'publication/README.md',
    'publication/repository-preparation.md', 'publication/licensing-checklist.md',
    'publication/security-checklist.md', 'publication/release-checklist.md',
    'publication/founder-approval.md',
    'assets/README.md', 'assets/branding/arc-logo.svg', 'assets/branding/arc-logo.png',
    'assets/branding/arc-logo-icon.png', 'assets/branding/manifest.json',
    'licenses/CC-BY-NC-4.0.txt', 'tools/LICENSE', 'docs/education/README.md', '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/engineering-proposal.md', '.github/ISSUE_TEMPLATE/config.yml',
]

def validate(profile=None):
    errors = []
    warnings = []
    candidate_names = subprocess.check_output(['git','-C',str(ROOT),'ls-files','--cached','--others','--exclude-standard','-z']).decode().split('\0')
    files = sorted({ROOT / name for name in candidate_names if name and (ROOT / name).is_file()})
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f'Missing required file: {name}')
    license_file = ROOT / 'licenses/PolyForm-Noncommercial-1.0.0.txt'
    if not license_file.exists() or hashlib.sha256(license_file.read_bytes()).hexdigest() != LICENSE_SHA256:
        errors.append('Official license byte hash does not match verified download')
    cc_file = ROOT / 'licenses/CC-BY-NC-4.0.txt'
    if not cc_file.exists() or hashlib.sha256(cc_file.read_bytes()).hexdigest() != CC_SHA256:
        errors.append('Official CC BY-NC legal-code hash mismatch')
    mit_file = ROOT / 'tools/LICENSE'
    if not mit_file.exists() or hashlib.sha256(mit_file.read_bytes()).hexdigest() != MIT_SHA256:
        errors.append('Scoped MIT license hash mismatch')
    if 'SPDX-License-Identifier: MIT' not in (ROOT/'tools/validate_docs.py').read_text():
        errors.append('Validator MIT source notice missing')
    for path in ('README.md','LICENSING.md','COPYRIGHT.md','tools/README.md'):
        if 'MIT' not in (ROOT/path).read_text():
            errors.append(f'Validator MIT scope reference missing: {path}')
    links = 0
    # Narrow token patterns plus explicit private-key/service-account markers.
    # Generic words such as "key" or documentation examples are not secrets.
    patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}',
                r'AKIA[A-Z0-9]{16}', r'AIza[A-Za-z0-9_-]{35}',
                r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                r'"type"\s*:\s*"service_account"',
                r'"private_key"\s*:\s*"[^\"]+']
    for p in files:
        name = str(p.relative_to(ROOT))
        if p.suffix not in ('.md', '.txt', '.yml', '.py', '.json', '.png', '.svg') and p.name not in ('.gitignore', '.gitattributes', 'LICENSE'):
            errors.append(f'Unexpected publication artifact: {name}')
            continue
        if p.suffix == '.png':
            raw = p.read_bytes()
            if raw[:8] != b'\x89PNG\r\n\x1a\n' or len(raw) < 26 or raw[25] != 6:
                errors.append(f'Branding PNG must preserve RGBA transparency: {name}')
            continue
        text = p.read_text(encoding='utf-8')
        if not text.strip():
            errors.append(f'Empty file: {name}')
        for pattern in patterns:
            if re.search(pattern, text):
                errors.append(f'Possible secret pattern in {name}; inspect privately')
        if p.suffix == '.md' and ('/Users/' in text or '/home/' in text or 'plugin://' in text):
            errors.append(f'Private machine/session reference in {name}')
        if p.suffix == '.md':
            rendered_text = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
            destinations = re.findall(r'\[[^\]]*\]\(([^)]+)\)', rendered_text) + re.findall(r'<img[^>]+src=[\"\']([^\"\']+)', rendered_text)
            for dest in destinations:
                dest = dest.strip().split(' ', 1)[0].strip('<>')
                parsed = urlsplit(dest)
                if parsed.scheme or dest.startswith('//'):
                    continue
                target = (p.parent / unquote(parsed.path)).resolve() if parsed.path else p
                try:
                    target.relative_to(ROOT)
                except ValueError:
                    errors.append(f'Link escapes repository in {name}: {dest}')
                    continue
                links += 1
                if not target.exists():
                    errors.append(f'Broken local link in {name}: {dest}')
    for name in ('README.md', 'COPYRIGHT.md', 'LICENSING.md', 'COMMERCIAL_LICENSING.md', 'GOVERNANCE.md'):
        text = (ROOT / name).read_text()
        if OWNER not in text or 'ARC Motion & Light' not in text:
            errors.append(f'Inconsistent legal identity: {name}')
        if not re.search(r'\bCVR:\s*34843341\b', text.replace('*','')) or 'DK34843341' in text:
            errors.append(f'CVR must be presented as CVR: 34843341: {name}')
    registry = (ROOT / 'repositories/repository-registry.md').read_text()
    for name in ['arc-stm32g4-lamp-firmware', 'arc-stm32g4-motor-firmware',
                 'arc-stm32wba-lamp-firmware', 'arc-stm32wba-probe-firmware',
                 'arc-stm32wba-gateway-firmware', 'arc-stm32wba-remote-controller-firmware']:
        if name not in registry:
            errors.append(f'Missing planned repository: {name}')
    for name in ('README.md', 'COPYRIGHT.md', 'LICENSING.md', 'licenses/DOCUMENTATION_LICENSE_REVIEW.md'):
        if 'CC BY-NC 4.0' not in (ROOT / name).read_text():
            errors.append(f'Missing approved documentation-license reference: {name}')
    for name in ('LICENSING.md', 'TRADEMARKS.md', 'assets/README.md'):
        text = (ROOT / name).read_text().lower()
        if 'all rights reserved' not in text or 'branding' not in text:
            errors.append(f'Missing branding rights exclusion: {name}')
    manifest = json.loads((ROOT / 'assets/branding/manifest.json').read_text())
    for item in manifest['files']:
        asset = ROOT / item['path']
        if not asset.exists() or hashlib.sha256(asset.read_bytes()).hexdigest() != item['sha256']:
            errors.append(f'Brand asset hash mismatch: {item["path"]}')
        if asset.suffix == '.png':
            w,h = struct.unpack('>II', asset.read_bytes()[16:24])
            if [w,h] != item['size']:
                errors.append(f'Brand asset dimensions mismatch: {item["path"]}')
    svg = ET.fromstring((ROOT / 'assets/branding/arc-logo.svg').read_text())
    if svg.attrib.get('viewBox') != '0 0 64 58' or any(e.tag.split('}')[-1] not in ('svg','title','desc','path') for e in svg.iter()):
        errors.append('Unexpected alteration or active content in brand SVG')
    for item in manifest['files']:
        tracked = subprocess.run(['git','-C',str(ROOT),'ls-files','--error-unmatch',item['path']],capture_output=True)
        if tracked.returncode:
            errors.append(f'Brand asset not tracked/staged: {item["path"]}')
    if profile is not None:
        expected_profile = {'profile/assets/arc-logo.png':'assets/branding/arc-logo.png',
                            'assets/branding/arc-logo-icon.png':'assets/branding/arc-logo-icon.png',
                            'licenses/CC-BY-NC-4.0.txt':'licenses/CC-BY-NC-4.0.txt'}
        if not (profile / 'profile/README.md').is_file():
            errors.append('Separate organization-profile staging package missing')
        else:
            profile_text = (profile / 'profile/README.md').read_text()
            for token in ('ARC Motion & Light','CC BY-NC 4.0','34843341','juan@arcstore.io','arc-open-development'):
                if token not in profile_text:
                    errors.append(f'Staged profile missing {token}')
            if OWNER not in profile_text or 'all rights reserved' not in profile_text.lower():
                errors.append('Staged profile attribution/branding scope missing')
            for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)', profile_text):
                if not urlsplit(dest).scheme:
                    links += 1
                    if not (profile / 'profile' / unquote(dest)).is_file():
                        errors.append(f'Broken profile image/reference: {dest}')
        for staged,original in expected_profile.items():
            if not (profile/staged).is_file() or (profile/staged).read_bytes() != (ROOT/original).read_bytes():
                errors.append(f'Staged profile asset/license mismatch: {staged}')
        if (profile/'.git').exists() and subprocess.check_output(['git','-C',str(profile),'remote'],text=True).strip():
            errors.append('Staged profile has a remote before approval')
    remotes = subprocess.check_output(['git', '-C', str(ROOT), 'remote'], text=True).strip()
    # Remotes are reported rather than rejected: the checker must also work
    # in a future approved public clone. This task does not configure one.
    for name in PRIVATE_REPORTS:
        if (ROOT/name).exists():
            errors.append(f'Internal review report remains in public tree: {name}')
    for name in ('phase-1-review.md', 'phase-1b-review.md'):
        private = '.review/publication/' + name
        tracked = subprocess.run(['git','-C',str(ROOT),'ls-files','--error-unmatch',private],capture_output=True)
        if tracked.returncode == 0:
            errors.append(f'Private review record is tracked: {private}')
        ignored = subprocess.run(['git','-C',str(ROOT),'check-ignore','--quiet',private],capture_output=True)
        if ignored.returncode != 0:
            errors.append(f'Private review record is not Git-ignored: {private}')
    historical = subprocess.check_output(['git','-C',str(ROOT),'log','--all','--format=%H','--',*PRIVATE_REPORTS],text=True).strip()
    if historical:
        warnings.append('Earlier commits contain internal review reports; exclude them through a separately approved sanitized publication history/export before a public push.')
    if (ROOT / 'LICENSE').exists() or (ROOT / '.github/profile/README.md').exists():
        errors.append('Blanket root license or incorrectly placed organization profile')
    result = {'files_checked': len(files), 'local_links_checked': links,
              'license_sha256': LICENSE_SHA256, 'cc_license_sha256': CC_SHA256, 'mit_license_sha256': MIT_SHA256,
              'profile_package_checked': profile is not None, 'remote_configured': bool(remotes),
              'private_review_history_present': bool(historical), 'warnings': warnings,
              'errors': errors, 'scope': 'Offline documentation checks; not a legal/security clearance'}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile-package', type=Path, help='Optional separately staged organization-profile package')
    args = parser.parse_args()
    sys.exit(validate(args.profile_package.resolve() if args.profile_package else None))
