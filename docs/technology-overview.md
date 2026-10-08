# Technology overview

ARC develops cooperating embedded applications rather than one monolithic firmware image. The Lamp prototype combines a STM32G4 real-time controller, STM32WBA5 communications controller, retained telemetry and an application/backend layer. Separate Probe, gateway, motion and remote applications have independent lifecycles.

The G4 controls PWM and the power stage, monitors thermal state, manages fans and determines whether commands are safe to apply. The WBA handles BLE and Thread, exchanges bounded messages with G4 and owns the current telemetry journal. Optional cloud synchronization supplements local acquisition; it is not the source of routine device recording.

Environmental sensing adds measurements to this platform. It must not bypass controller safety or turn a transport address into proof of device ownership. Account-level claiming/grants and device-local assignment are distinct trust boundaries.

[Architecture](../architecture/platform-overview.md) describes these responsibilities. [Product families](../products/README.md) and [development status](development-status.md) distinguish prototype evidence from proposed applications. WBA5 is the present development generation; WBA6 is a planned compatibility target with no verified build or hardware claim here.
