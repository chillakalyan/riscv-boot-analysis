


# RISC-V Boot Analysis Toolkit

This repository explores the early boot process of a **RISC-V Linux system** running in **QEMU** with **OpenSBI firmware**.
The goal is to analyze architectural state transitions during boot and investigate the minimal processor state required for **checkpoint-based RTL simulation**, particularly for platforms such as **OpenPiton**.

## Overview

Modern RTL simulators can take a long time to boot a full operating system.
Checkpointing allows the simulator to restore execution from a saved architectural state instead of repeating the entire boot process.

This project documents experiments and observations related to:

* RISC-V privilege mode transitions
* OpenSBI firmware initialization
* Control and Status Register (CSR) state during boot
* QEMU debugging using GDB
* Architectural state inspection for checkpointing

## RISC-V Boot Flow

The following diagram illustrates the high-level boot sequence of a RISC-V system running in QEMU with OpenSBI.

![RISC-V Boot Flow](images/riscv_boot_flow.png)

## Architectural Checkpoint State

The following diagram illustrates the concept of capturing the minimal
architectural state of a RISC-V processor so that execution can be resumed
without repeating the entire boot process.

In long RTL simulations (e.g., OpenPiton), checkpointing allows the system
to restore processor state and continue execution from a saved point,
significantly reducing simulation time.

![Architectural Checkpoint State](images/checkpoint_state_architecture.png)


To accelerate RTL simulations, the processor state can be checkpointed after the system completes its early boot phase.

This repository investigates the **minimal architectural state required to resume execution**, including:

* Program counter (PC)
* General-purpose registers
* Control and Status Registers (CSR)
* Privilege mode state

Detailed analysis is available here:

docs/checkpoint_state.md

## Boot State Experiment

An experiment was conducted to capture architectural processor state
during the early boot phase using QEMU and GDB.

The goal was to observe how processor registers and control state
change during system initialization and identify the minimal state
required for checkpoint-based simulation.

Example architectural state observed during boot:

pc       = 0x8000b64a  
satp     = 0x0  
mstatus  = 0xa00000000  
medeleg  = 0x0  
mideleg  = 0x1444  

More details are available here:

docs/boot_state_experiment.md

## Environment

The experiments were performed using the following tools:

* QEMU (RISC-V virt machine)
* OpenSBI firmware
* Linux kernel (RISC-V)
* gdb-multiarch for debugging

## Key Findings

From the experiments and architectural inspection performed using QEMU and GDB, the following observations were made:

- During early boot, the processor executes in **Machine Mode (M-mode)** under the control of OpenSBI firmware.
- The **satp register remains 0**, indicating that virtual memory is not enabled at the early boot stage.
- The **mstatus register configures machine-level execution state** before the transition to supervisor mode.
- **Trap delegation registers (medeleg and mideleg)** determine which exceptions and interrupts are forwarded to supervisor mode.
- After OpenSBI initialization, control is transferred to the **Linux kernel in Supervisor Mode (S-mode)**.

These observations help identify the **minimal architectural processor state required for checkpoint-based simulation**, which can significantly reduce boot overhead in RTL simulation platforms such as OpenPiton.


### Folder Description

- **docs/** – Detailed documentation explaining the RISC-V boot process, CSR analysis, debugging steps, and checkpoint architecture.
- **images/** – Architecture diagrams used in the documentation.
- **logs/** – Boot logs collected during QEMU experiments.
- **scripts/** – Helper scripts used to extract architectural state using GDB.
- **LICENSE** – MIT license for the project.
- **README.md** – Project overview and documentation entry point.

## Repository Structure
```
riscv-boot-analysis/
|
├── docs/
| ├── boot_sequence.md
│ ├── boot_state_experiment.md
│ ├── checkpoint_state.md
│ ├── csr_analysis.md
│ ├── gdb_debugging.md
│ └── qemu_setup.md
│
├── images/
│ ├── checkpoint_state_architecture.png
│ └── riscv_boot_flow.png
│
├── logs/
│ └── linux_boot.txt
│
├── scripts/
│ └── dump_registers.py
│
├── LICENSE
└── README.md
```
## Future Work

Possible extensions of this work include:

- Automating architectural state extraction using GDB scripts
- Identifying the minimal checkpoint state required for OpenPiton RTL simulation
- Experimenting with restoring processor state during simulation
- Integrating checkpointing mechanisms into the OpenPiton simulation flow

## References

- RISC-V Privileged Architecture Specification  
  https://riscv.org/technical/specifications/

- OpenSBI Firmware  
  https://github.com/riscv-software-src/opensbi

- QEMU RISC-V Documentation  
  https://www.qemu.org/docs/master/system/target-riscv.html

- OpenPiton Project  
  https://github.com/PrincetonUniversity/openpiton

