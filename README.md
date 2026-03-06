# RISC-V Boot Analysis Toolkit

This repository documents experiments exploring the boot sequence
of a RISC-V Linux system running in QEMU with OpenSBI firmware.

The goal is to understand architectural state transitions during
early boot and analyze the minimal processor state required for
checkpointing in RTL simulations such as OpenPiton.

Topics explored:

• RISC-V privilege modes  
• OpenSBI firmware initialization  
• CSR state transitions  
• QEMU debugging using GDB  
• Architectural state inspection

## RISC-V Boot Flow

The following diagram illustrates the early boot sequence of a
RISC-V system running in QEMU with OpenSBI firmware.

![RISC-V Boot Flow](images/riscv_boot_flow.png)

## Architectural Checkpoint State

For faster RTL simulation in platforms such as OpenPiton,
the system state can be checkpointed after the boot phase.

This repository explores the minimal architectural state
required to restore processor execution.

See detailed analysis here:

docs/checkpoint_state.md

Environment:

QEMU
OpenSBI
Linux Kernel (RISC-V)
gdb-multiarch

Repository Structure:

docs/
Documentation and analysis

logs/
Captured boot logs

scripts/
Automation scripts for debugging

images/
Architecture diagrams
