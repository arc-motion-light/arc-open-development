# Development status

Snapshot: 8 October 2026. This is a bounded engineering overview, not product certification, production acceptance or a support promise.

| Capability | Technical maturity | Evidence / limitation |
|---|---|---|
| G4 Lamp PWM, thermal/fan control and RTC | Implemented and demonstrated on the Lamp prototype | Private source, dated validation notes and bench observations |
| G4–WBA DMA communication | Implemented and demonstrated | Existing integration build and current bench diagnostics |
| WBA Flash Lamp and Probe history with BLE retrieval | Implemented; Probe recovery reported | Existing Lamp tests/bench evidence plus founder-reported restored Probe path; unique Probe records reported accepted without the former five-minute historian gate |
| Independent Lamp history cadence | Implemented with bounded bench validation | Device ACKs for 60/300 seconds and retained count progression; app UI acceptance and cold-power system recovery are not implied |
| Probe measurements and Thread route | Recovered end-to-end operation reported | Phase 1B founder brief reports rejoin, WBA reception/history commit and iOS display after a temporary configuration regression; independent release evidence/endurance review remains pending |
| Backend claim/ownership/DeviceGrants | Existing implemented dependency | Selected permission/claim regression suites; not proof of hardware authentication |
| Persistent authorized Probe binding | Under development | Standalone 16-entry tests; no accepted live authorization/persistence bridge |
| Cold-power Thread settings restoration | Under development | SRAM-backed settings observed; no complete durable backend accepted |
| WBA6 compatibility | Planned | No reproducible compilation or physical validation recorded |
| Motor, standalone gateway and touch remote publication | Planned | Separate repository/source/maturity audits required |

The 8 October 2026 Phase 1B directive supersedes the earlier detached diagnostic snapshot. It is the source for the reported recovery and Probe-gate change, not independent proof of a published release or long-term endurance. The inspected Lamp workspace snapshot still contains a five-minute Probe retention branch, so the exact recovered build/source reference must be reconciled before firmware publication; no firmware is changed here.

Registration, network attachment and actual recording are separate states. A known sleeping Probe should remain registered; joining a network is not a claim or approved assignment. [Provenance](../provenance/development-history.md) identifies the evidence basis without exposing private logs or device identifiers.

All firmware publication states remain **Planned** in this Phase 1 package, independently of their technical maturity.
