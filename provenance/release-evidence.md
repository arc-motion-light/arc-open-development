# Required release evidence

Future releases should retain this record privately and publish a sanitized counterpart:

| Field | Required content |
|---|---|
| Source | Original repository/commit, public candidate and mapping method |
| Authorship/rights | ARC material, contributors, dependencies and applicable notices |
| Hardware | Exact board revision and MCU; omit deployed serial numbers |
| Build | Toolchain, SDK, configuration, command, result and relevant warnings |
| Artifact | Filename, SHA-256 and linked/programmed region audit |
| Tests | Exact host tests and real bench procedures, results and limitations |
| Persistence | Regions owned, update/recovery behavior and destructive operations excluded |
| Security | Audit scope, secret-handling evidence, unresolved limitations and reviewer |
| Approval | Named approver, scope, candidate commit and actual decision date |
| Publication | Public location, tag/commit and publication date after publication occurs |

A checksum proves file identity, not safety, ownership or correct behavior. A build log does not prove hardware acceptance. Logs containing credentials, personal data or raw device memory are private evidence and must be sanitized before any public use.

No firmware release evidence package is completed in Phase 1. The [history overview](development-history.md) is deliberately narrower.
