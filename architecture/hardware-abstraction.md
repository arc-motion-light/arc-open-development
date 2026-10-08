# Hardware abstraction and target compatibility

ARC aims to separate application behavior from board-specific pins, peripheral instances, radio stacks, memory geometry and power-management configuration. Reuse requires explicit target adapters and validation, not broad preprocessor substitutions.

| Target family | Current evidence | Upgrade position |
|---|---|---|
| STM32G4 Lamp / STSPIN32G4 | Existing real-time Lamp prototype and integration build | New boards need their own pin, power-stage and safety review |
| STM32WBA5 Lamp | Existing connectivity/history prototype | Exact device and SDK remain target-specific |
| STM32WBA5 Probe | Candidate source builds and existing deployed diagnostics | Recovered telemetry reported; exact recovered-build evidence remains to be reconciled |
| STM32WBA6 | Planned | Compilation and hardware tests pending |

Future firmware repositories must record exact MCU/board, toolchain, vendor SDK, build configuration and command, compilation result and hardware-test result separately. Include unsupported targets explicitly. An SDK containing a device definition is not proof that ARC firmware builds or runs on it.

Memory boundaries, boot/update mechanisms and credential storage must be audited per target. A safe Flash region on one board is not permission to allocate the same addresses on another. See [repository naming](../repositories/naming-conventions.md).
