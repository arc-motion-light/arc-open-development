# Firmware README template

Use this structure in a separately audited repository. Replace every bracketed value with verified evidence before publication. Remove irrelevant sections rather than implying all ARC applications share one design.

```markdown
# [repository name]

[Application responsibility and exact supported board.]

## Status
Publication state: [Planned / In preparation / Under review / Ready for publication / Published / Archived]
Technical maturity: [implemented/demonstrated, under development, or planned; evidence and limits]

## Architecture and safety
[Control, connectivity, configuration, historian and credential ownership.]
[Application-specific safety authority and external-command boundaries.]

## Compatibility
| Exact target/board | SDK | Build configuration | Build result | Hardware validation |
|---|---|---|---|---|
| [WBA5 or G4 target] | [version] | [configuration] | [actual result] | [actual bench result or Pending] |
| [WBA6, if in scope] | [version or Pending] | [configuration or Pending] | Pending | Pending |

## Reproducible build
[Toolchain version, prerequisites, exact build command, source commit and warnings.]

## Tests and safe deployment
[Host commands, bench procedures, image-region audit and retention/recovery limits.]
[Do not provide erase/reset instructions without ownership and preservation evidence.]

## Licensing and rights
[ARC-owned paths designated for PolyForm Noncommercial 1.0.0.]
[Third-party paths remain governed by their own licenses and notices.]
[Original ARC public documentation: CC BY-NC 4.0, with supplied attribution and modification notices.]
[Branding: all rights reserved; executable tooling, hardware and third-party material remain separately governed.]

## Provenance and contributions
[Original/private-to-public mapping and reviewed contributor arrangement.]

## Commercial licensing and security
Commercial inquiries: juan@arcstore.io
[Private security reporting and supported-version policy, if established.]
```

Required companion files normally include `LICENSE`, `COPYRIGHT.md`, `THIRD_PARTY_NOTICES.md`, `COMMERCIAL_LICENSING.md`, `CONTRIBUTING.md`, `SECURITY.md` and `DEVELOPMENT_HISTORY.md`. Copy the [official license](../licenses/PolyForm-Noncommercial-1.0.0.txt) byte-for-byte into firmware `LICENSE` only after scope/rights review. See [release evidence](../provenance/release-evidence.md).
