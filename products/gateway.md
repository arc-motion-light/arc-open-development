# Standalone gateway

The standalone gateway application is intended to connect ARC devices and application services independently of the Lamp's real-time controller. Its firmware lifecycle and publication review remain separate from the Lamp WBA image.

A shared MCU family or vendor SDK does not make gateway routing, cloud delivery or power behavior equivalent to the Lamp prototype. This Phase 1 review does not validate a gateway release, network topology, NB-IoT deployment or supported commercial configuration.

The proposed `arc-stm32wba-gateway-firmware` remains Planned for publication. Its future audit must identify source, hardware, transport responsibilities, credential ownership and actual build/bench evidence. No gateway repository is created in this task.
