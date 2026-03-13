# RISC-V Boot Analysis Toolkit

This repository explores the early boot process of a **RISC-V Linux system** running in **QEMU** with **OpenSBI firmware**.

The goal of this project is to analyze architectural state transitions during boot and investigate the **minimal processor state required for checkpoint-based RTL simulation**, particularly for platforms such as **OpenPiton**.

Checkpointing allows a simulator to restore execution from a saved architectural state instead of repeating the entire operating system boot process, significantly reducing simulation time.

---

# Overview

Modern RTL simulators require a large number of cycles to boot a full operating system such as Linux.

Instead of simulating the entire boot sequence repeatedly, checkpointing enables:

- capturing processor architectural state at a stable execution point
- saving this state to a checkpoint file
- restarting simulation from the saved state

This project investigates how such checkpointing can be applied to **RISC-V systems running Linux under QEMU**.

---

# Topics Explored

This repository documents experiments and observations related to:

- RISC-V privilege mode transitions
- OpenSBI firmware initialization
- Control and Status Register (CSR) behavior during boot
- QEMU debugging using GDB
- architectural state inspection for checkpointing
- analysis of checkpointing mechanisms in virtualization and OS hibernation

---

# RISC-V Boot Flow

The following diagram illustrates the high-level boot sequence of a RISC-V system running in QEMU with OpenSBI.

![RISC-V Boot Flow](images/riscv_boot_flow.png)

Boot stages:

1. CPU reset
2. OpenSBI firmware initialization
3. Machine mode configuration
4. Trap delegation (medeleg / mideleg)
5. Transition to supervisor mode
6. Linux kernel entry

---

# Architectural Checkpoint Concept

The following diagram illustrates the concept of capturing the minimal architectural state of a RISC-V processor so that execution can resume without repeating the entire boot process.

![Architectural Checkpoint State](images/checkpoint_state_architecture.png)

Checkpointing enables the simulator to restore processor state and continue execution from a previously saved point.

The minimal checkpoint state typically includes:

- Program Counter (PC)
- General-purpose registers
- Control and Status Registers (CSR)
- Privilege mode state
- relevant memory state

More details:
```
docs/checkpoint_state.md
```

---

# Boot State Experiment

An experiment was conducted to observe architectural processor state during early boot using **QEMU and GDB**.

The objective was to inspect register values and system state transitions during initialization.

Example architectural state observed during boot:
```
pc = 0x8000b64a
satp = 0x0
mstatus = 0xa00000000
medeleg = 0x0
mideleg = 0x1444
```

These observations help identify the minimal architectural state required for checkpoint-based simulation.

Detailed experiment documentation:
```
docs/boot_state_experiment.md
```

---

# Key Findings

From the experiments and architectural inspection performed using QEMU and GDB, the following observations were made:

- The processor begins execution in **Machine Mode (M-mode)** under OpenSBI firmware.
- The **satp register remains 0 during early boot**, indicating that virtual memory has not yet been enabled.
- The **mstatus register configures machine-level execution state** prior to privilege transitions.
- **medeleg and mideleg registers** define which exceptions and interrupts are delegated to supervisor mode.
- After OpenSBI initialization, execution transitions to the **Linux kernel running in Supervisor Mode (S-mode)**.

Understanding these transitions helps determine the **minimal processor state required to restart execution in RTL simulations**.

---

# Environment

The experiments were performed using the following tools:

- QEMU (RISC-V virt machine)
- OpenSBI firmware
- Linux Kernel (RISC-V)
- gdb-multiarch

---

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
│
├── docs/
│   ├── architecture_overview.md
│   ├── boot_sequence.md
│   ├── boot_state_experiment.md
│   ├── boot_state_transition.md
│   ├── checkpoint_flow.md
│   ├── checkpoint_state.md
│   ├── csr_analysis.md
│   ├── gdb_debugging.md
│   ├── gdb_state_capture.md
│   ├── linux_hibernation_analysis.md
│   ├── minimal_checkpoint_state.md
│   ├── opensbi_linux_transition.md
│   ├── paper_notes.md
│   ├── qemu_checkpointing.md
│   ├── qemu_setup.md
│   ├── references.md
│   └── related_work.md
│
├── images/
│   ├── boot_state_transition.png
│   ├── checkpoint_flow.png
│   ├── checkpoint_state_architecture.png
│   └── riscv_boot_flow.png
│
├── logs/
│   └── linux_boot.txt
│
├── scripts/
│   ├── capture_checkpoint_state.py
│   └── dump_registers.py
│
├── LICENSE
└── README.md
```


---

# Future Work

Possible extensions of this work include:

- automating architectural state extraction using GDB scripts
- identifying the minimal checkpoint state required for OpenPiton RTL simulation
- implementing checkpoint restore mechanisms
- exploring integration of checkpointing into the OpenPiton simulation workflow
- investigating relationships between VM snapshots, Linux hibernation, and architectural checkpointing

---

# References

RISC-V Privileged Architecture Specification  
https://riscv.org/technical/specifications/

OpenSBI Firmware  
https://github.com/riscv-software-src/opensbi

QEMU RISC-V Documentation  
https://www.qemu.org/docs/master/system/target-riscv.html

OpenPiton Project  
https://github.com/PrincetonUniversity/openpiton

