# Security reporting and publication hygiene

Report suspected vulnerabilities privately to [juan@arcstore.io](mailto:juan@arcstore.io), with the affected component, version or commit, a minimal reproduction and likely impact. Do not include device credentials, personal telemetry, private keys or live provisioning data in public issues. Arrange a secure channel before sharing sensitive proof.

ARC has not established a public supported-version schedule, response SLA, bug bounty or formal disclosure timetable. Discuss coordination privately. This documentation repository contains no deployable firmware release.

Future publication reviews must inspect both the working tree and complete proposed history. Review network credentials, cloud/service tokens, signing keys, debug captures, crash dumps, provisioning identifiers and generated build outputs. Removing a secret from the current file does not remove it from history. If exposure is found, revoke or rotate affected secrets as appropriate; history cleanup alone is insufficient.

Existing backend ownership and grants must not be represented as complete hardware authorization. CRC checks detect accidental corruption; they do not authenticate assignments. Present unresolved local provisioning and cold-power persistence accurately.

Use [the security checklist](publication/security-checklist.md). A local pattern scan is one review input, not proof that a repository is safe to publish.
