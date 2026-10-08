# Battery-powered touch remote

The Remote Controller is an intended separate STM32WBA application on ARC's shared hardware platform. It is intended to use a touch interface and battery power to control compatible ARC devices.

A common platform does not imply a common firmware image or proven battery lifetime. Wake behavior, touch acquisition, radio activity, command authorization and target compatibility require independent design and measurement.

The proposed `arc-stm32wba-remote-controller-firmware` has its own lifecycle. Source maturity, build status and hardware validation are not established by this Phase 1 review. No remote firmware or hardware design is created or published here.

See [wireless architecture](../architecture/wireless-connectivity.md) and [publication registry](../repositories/repository-registry.md).
