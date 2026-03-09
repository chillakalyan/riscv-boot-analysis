# RISC-V Boot Sequence

This document describes the early boot process of a RISC-V Linux system
running in QEMU using OpenSBI firmware.

Understanding the boot sequence is important for identifying the
architectural processor state required for checkpoint-based execution
restart.

## Boot Flow Overview

CPU Reset  
↓  
OpenSBI Firmware Initialization  
↓  
Machine Mode (M-mode) Setup  
↓  
Trap Delegation (medeleg / mideleg)  
↓  
Transition to Supervisor Mode (S-mode)  
↓  
Linux Kernel Entry

## CPU Reset

When the system starts, the processor begins execution from the reset
vector. In the QEMU virt machine, this typically starts at address:

0x1000

Execution begins in **Machine Mode (M-mode)**, the highest privilege
level in the RISC-V architecture.

## OpenSBI Initialization

OpenSBI acts as the firmware layer responsible for:

- hardware initialization
- interrupt configuration
- platform setup
- privilege mode transition

OpenSBI prepares the environment required for the operating system.

## Machine Mode Configuration

During initialization, OpenSBI configures several Control and Status
Registers (CSRs), including:

- mstatus
- mtvec
- medeleg
- mideleg

These registers determine how traps and interrupts are handled.

## Trap Delegation

OpenSBI configures the following registers:

- **medeleg** – delegates exceptions to Supervisor Mode
- **mideleg** – delegates interrupts to Supervisor Mode

This allows the Linux kernel to manage most traps directly.

## Transition to Supervisor Mode

After initialization is complete, OpenSBI transfers control to the
Linux kernel in **Supervisor Mode (S-mode)**.

The kernel entry point address is provided by OpenSBI.

## Importance for Checkpointing

Understanding the boot sequence helps determine:

- when the system reaches a stable architectural state
- which registers must be captured for checkpointing
- how execution can be resumed in RTL simulation environments
