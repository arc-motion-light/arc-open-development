# Telemetry and data ownership

| Layer | Responsibility |
|---|---|
| G4 Lamp | Operational measurements, local safety and authoritative RTC reference |
| Wireless Probe | Environmental measurement and its own wake/report behavior |
| Lamp WBA | Measurement ingress, timestamp handling, serialized Flash commits and shared history sequence |
| Application | BLE history retrieval, local persistence and visualization |
| Cloud | Optional synchronization and account-level services where implemented |

The current historian is WBA Flash, using canonical 32-byte records plus storage integrity/commit metadata. G4 FRAM holds controller configuration rather than routine system-wide telemetry history. Lamp history recording must work with zero Probes and has an independent interval; live SPI/BLE traffic is not itself the commit cadence.

The Phase 1B brief reports removal of the former five-minute Probe historian gate: valid unique Probe measurements are retained without that extra recording delay. Sensor measurement/report cadence, sleepy-child polling and independent Lamp commit cadence remain distinct. The recovered source/build must be reconciled before firmware publication.

A shared sequence belongs to the historian and must survive ordinary recovery. Invalid timestamps remain explicitly marked. Phone receipt time must not silently replace a device timestamp and masquerade as recorded UTC. Retention depends on record rate, capacity and recovery behavior; no universal retention or reliability guarantee is made here.

Keep three concepts separate: **registered** is an approved persistent association, **attached** is network connectivity, and **recording** is successful history commit. The current history source catalog is not an ownership database. The live three-source limitation and standalone sixteen-entry registry are distinct unfinished capacity concerns.
