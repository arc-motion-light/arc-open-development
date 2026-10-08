# Naming and compatibility conventions

Firmware names follow `arc-<mcu-family>-<application>-firmware`.

Use `stm32g4` or `stm32wba` as the MCU family and a descriptive application name such as `lamp`, `motor`, `probe`, `gateway` or `remote-controller`. For WBA, avoid names tied to WBA5 alone or combined “WBA5-6” names. Board/generation differences belong in build configurations and compatibility tables.

The central documentation repository is `arc-open-development`. The special organization-profile repository is `.github`; it is not this repository's internal `.github/` metadata folder.

A future compatibility table must separate exact target, build status and hardware validation. Use Pending until a reproducible build or physical test exists. A family-level repository name is an organization decision, not an assertion of cross-generation compatibility.

Existing private directories are not renamed in Phase 1. Future migrations require their own provenance mapping and approval.
