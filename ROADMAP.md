# Development and publication roadmap

The following sequence is a preparation plan, not a release calendar or product-availability commitment.

| Phase | Scope | Gate |
|---|---|---|
| 1 | Central `arc-open-development` documentation foundation | Local validation, then founder review; no publication in this task |
| 2 | `arc-stm32g4-lamp-firmware` | Ownership, dependency, security, history and build audit |
| 3 | `arc-stm32wba-lamp-firmware` | Same audit plus retained-history/network preservation evidence |
| 4 | `arc-stm32wba-probe-firmware` | Identify deployed target, secure commissioning and power-management evidence |
| 5 | `arc-stm32g4-motor-firmware` | Independent motion-application source and maturity audit |
| 6 | `arc-stm32wba-gateway-firmware` | Independent gateway source and publication audit |
| 7 | `arc-stm32wba-remote-controller-firmware` | Independent battery/touch application audit |

The order can change with readiness. Each firmware repository needs its own release approval and must preserve its original private history.

WBA6 is a future compatibility target. Future WBA repositories should establish separate, reproducible WBA5 and WBA6 builds and report hardware validation independently. No WBA6 implementation or migration is part of Phase 1.

Reported Probe routing recovery precedes further work on durable secure onboarding, cold-power network settings, authenticated assignment-to-hardware integration and live capacity reconciliation. Exact recovered-build evidence must be reconciled before firmware publication. A host-tested registry is not a deployed binding system. See [status](docs/development-status.md) and [registry](repositories/repository-registry.md).
