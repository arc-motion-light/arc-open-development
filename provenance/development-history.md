# Initial development history

This timeline is an evidence inventory, not a complete company history or legal ownership opinion. Dates describe documented events; they are not reconstructed first-invention dates.

| Date | Supported milestone | Evidence basis and limit |
|---|---|---|
| 8 September 2026 | Lamp development snapshot assembled from separate controller/connectivity trees | Existing workspace README; not the beginning of all ARC development |
| 13 September 2026 | G4 fan PWM/tach/RPM development recorded | Private G4 commit `f72136d`; commit subject alone is not a complete hardware test |
| 29 September 2026 | G4 FRAM service and LSE RTC validation documented | `FRAM_MEMORY_LAYER.md` and `RTC_LSE_VALIDATION.md`; dated bench notes, not certification |
| 7 October 2026 | Local-first memory audit and staged WBA historian plan documented | Private architecture audit; contains proposals as well as observations |
| 8 October 2026 | G4 DMA/RTC/persistence and WBA historian/cadence development snapshots recorded | G4 `9daa82f892893aae16ed4284a72b457b0cd3905d`; workspace/WBA `3eff060b7c4b9079927dc8f7ce433986bb4b6870` |
| 8 October 2026 | Independent Lamp cadence bench returned persisted/effective settings and retained history progression | Private BLE bench: 60-second setting, two additional retained records, then 300-second restoration; broader UI/cold-power acceptance not established |
| 8 October 2026 | Probe recovery and recording-gate update reported | Founder Phase 1B directive; end-to-end recovery reported, exact recovered build/log reconciliation and endurance pending |
| 8 October 2026 | ARC Open Development Phase 1 documentation prepared locally | This repository's initial commit and privately retained review record |

The reviewed private source references are not public download links. Their original histories and supporting logs remain privately retained. The public summaries intentionally omit sensitive device/network details.

Earlier detached/zero-TX diagnostics describe a temporary regression. The Phase 1B founder directive reports subsequent Thread rejoin, WBA Flash Probe commits and iOS history display, and a historian change removing the extra five-minute Probe gate. This milestone is founder-reported; exact recovered source/artifact references and endurance evidence are pending reconciliation. Earlier June milestones and other product families remain pending evidence review rather than being assigned speculative dates.
