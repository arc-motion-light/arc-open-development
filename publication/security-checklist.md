# Security review checklist

- [ ] Inspect both present files and complete proposed history/tags/LFS objects.
- [ ] Exclude private internal review records from both the public tree and the history intended for publication; ignore rules do not remove earlier committed copies.
- [ ] Check credentials, service-account files, tokens, signing/private keys and provisioning material.
- [ ] Review embedded network defaults and debug examples; do not publish operational datasets.
- [ ] Exclude raw flash/SRAM/FRAM captures, user telemetry and device-linked identifiers.
- [ ] Remove confidential business/investor documents and private agreements from the candidate.
- [ ] Review URLs, generated files, screenshots, attachments and binary metadata.
- [ ] Inspect logo/derived-asset metadata and verify that source artwork is unchanged.
- [ ] Exclude unrelated files from the original branding/investor directory; import only approved logo files.
- [ ] Verify that staged organization-profile content contains no private paths, identifiers or live provisioning details.
- [ ] Record scanner version/scope and manually assess findings; never treat “zero matches” as a complete security audit.
- [ ] If a secret was exposed, handle revocation/rotation; removal alone is insufficient.
- [ ] Describe unresolved local authentication and recovery limitations accurately.
- [ ] Retain an approved private evidence record and safe public summary.

Use [SECURITY](../SECURITY.md) for private reporting. Phase 1 includes documentation-only checks; future firmware history requires its own review.
