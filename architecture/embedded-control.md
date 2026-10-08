# Real-time embedded control

The demonstrated Lamp application targets STM32G4 through the STSPIN32G4 controller platform. It runs bounded control, sampling and peripheral work with explicit separation from communications tasks.

Responsibilities include PWM/power-stage operation, temperature monitoring, output limiting, fan PWM and tachometer handling, controller configuration and RTC operation. Local hardware faults and thermal limits take priority over requested output. Incoming wireless commands or environmental measurements cannot override this safety authority.

An external low-frequency crystal supplies the Lamp RTC; it is distinct from the high-speed system/PWM clock. Timestamp validity must be explicit rather than treating an initialized calendar as trustworthy UTC.

The current integration build is known privately as `lamp_integration_dma`. Publication must separately document its exact board, dependencies, flags and acceptance limits; a build name is not a product certificate.

Motor control is an intended separate application family. Its loop timing, peripherals, power stages and safety requirements need their own design and validation. Do not infer a working motor product from Lamp PWM evidence.
