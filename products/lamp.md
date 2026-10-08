# Lamp

The Lamp is the current demonstrated reference for ARC's split embedded architecture. STM32G4 handles PWM/power-stage behavior, thermal limits, fans and RTC; STM32WBA5 handles communication and retained history.

The application retrieves device history and presents operating data. Optional cloud synchronization does not replace local acquisition. Independent Lamp commit cadence must remain available without any Probe.

Existing bench evidence covers selected control, RTC, DMA link and history behaviors. It does not establish production certification, broad electrical compliance, commercial availability or acceptance on every board. Current work includes operational verification, recovery and secure integration with Probe assignments.

Potential lighting applications include people, plants and built environments. Those markets require their own product, safety and performance evaluation. Planned public software is split into [G4 Lamp and WBA Lamp repositories](../repositories/repository-registry.md).
