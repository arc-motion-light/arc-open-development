# Repository registry

This registry is the publication index for ARC Open Development. Publication state describes distribution status, independently of technical maturity. Prepared names are not assertions that a public repository or release exists.

| Repository | Responsibility | Publication state | Technical maturity |
|---|---|---|---|
| [arc-open-development](https://github.com/arc-motion-light/arc-open-development) | Central documentation, architecture, licensing and publication policies | Published | Documentation foundation published on 8 October 2026; firmware releases remain independently reviewed |
| `arc-stm32g4-lamp-firmware` | Lamp real-time control | Planned | Existing prototype; independent publication audit pending |
| `arc-stm32g4-motor-firmware` | Motor/motion application | Planned | Pending separate source and hardware assessment |
| `arc-stm32wba-lamp-firmware` | Lamp connectivity and historian | Planned | Existing WBA5 prototype; recovery/security work and publication review continue |
| `arc-stm32wba-probe-firmware` | Environmental sensing Probe | Planned | Restored telemetry reported; recovered-build evidence and durable secure onboarding review pending |
| `arc-stm32wba-gateway-firmware` | Standalone connectivity gateway | Planned | Pending independent source, build and hardware audit |
| `arc-stm32wba-remote-controller-firmware` | Battery/touch control application | Planned | Intended family; validation pending |
| [Organization .github](https://github.com/arc-motion-light/.github) | Public organization profile | Published | Official profile content published on 8 October 2026; live avatar changes require separate authorization |

When an approved repository is actually published, change its state to **Published** and add the verified public URL and release/provenance references. Do not mark a row Published in anticipation of a push. Until then, proposed firmware names remain plain text rather than download links.

WBA5 is the current development generation; WBA6 remains unverified. Family-level names intentionally avoid generation numbers. See [publication states](publication-policy.md), [current development status](../docs/development-status.md) and [the roadmap](../ROADMAP.md).
