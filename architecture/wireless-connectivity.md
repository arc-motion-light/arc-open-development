# Wireless connectivity

STM32WBA5 is the current ARC Lamp communications development platform. BLE connects the application to device controls and history; Thread provides an environmental-measurement transport; a bounded controller link exchanges Lamp status, configuration operations and time references.

STM32WBA6 is an intended upgrade generation. Family-level naming supports separate targets, but source organization alone does not establish compatibility.

Network commissioning, backend account authorization and physical Probe assignment are separate operations. The existing Probe role-policy command is not evidence of installing a network dataset or committing a Lamp association. A successful BLE write is transport completion, not durable assignment acknowledgment.

A temporary Probe attachment regression was associated with network configuration. The Phase 1B brief reports successful rejoin and restored telemetry reception, history commits and iOS display. The former detached diagnostic must not be described as a permanent state. Exact recovered-build evidence and long-term endurance remain separate review items. Publication must explain limits without disclosing operational datasets or device identifiers.

Current Thread settings use SRAM-backed platform storage in the audited target. Warm preservation is not cold-power durability. A persistent implementation requires safe NVM ownership and atomic recovery. Never treat an apparently spare BLE/system page as an available credential store.
