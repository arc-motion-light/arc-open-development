# Wireless environmental Probe

The Probe development platform uses STM32WBA and sensor/power-management integration to measure environmental conditions. Its measurement cadence, UDP reporting cadence and sleepy-child polling are separate behaviors.

The Phase 1B founder brief reports that the Probe rejoined Thread after a temporary network-configuration regression. Measurements were again received by WBA5, committed to its Flash historian and displayed in iOS. It also reports acceptance of valid unique Probe records without the former five-minute historian gate. Earlier detached/zero-TX readings remain historical evidence, not the current status.

Exact recovered-build/log references remain to be reconciled for publication, and this recovery is not an uninterrupted endurance result. A role-policy write alone is still not proof of network commissioning or durable authorized assignment.

Autonomous operation requires an authenticated commissioning path, persistent network settings on the Probe and a verified physical assignment lifecycle. Stable canonical identity must remain distinct from BLE peripheral IDs and transient Thread addresses.

The sixteen-entry registry has standalone tests; it is not proof of deployed authorization, sixteen simultaneously attached children or sixteen independently recorded sources. These limits need separate verification in the future [Probe firmware preparation](../ROADMAP.md).
