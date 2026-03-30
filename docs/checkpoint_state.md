# Architectural Checkpoint Stat

Checkpointing allows a simulator to restore execution from a saved
processor state instead of repeating the entire boot process.

In RTL simulations such as OpenPiton, booting a full Linux system can
take a very long time. Capturing the minimal architectural state allows
the system to resume execution quickly.

## Required Architectural State

A minimal checkpoint state must capture the processor execution
context.

### Program Counter

The **Program Counter (PC)** contains the address of the next
instruction to execute.

Without restoring the correct PC, execution cannot resume properly.

### General Purpose Registers

RISC-V processors include 32 general purpose registers:
```
x0 – x31
```
These registers store intermediate computational values and must be
restored during checkpoint recovery.

### Control and Status Registers (CSRs)

Several CSRs control processor behavior and privilege configuration.

Important examples include:
```
- mstatus
- satp
- mtvec
- mepc
- medeleg
- mideleg
```
These registers define interrupt handling, privilege state, and memory
translation.

### Privilege Mode

The processor must restore the correct privilege level:
```
- Machine Mode (M-mode)
- Supervisor Mode (S-mode)
```
Linux typically runs in Supervisor Mode.

### Memory Context

If virtual memory is enabled, the page table configuration referenced
by the `satp` register must also be restored.

## Goal

The objective is to identify the **minimal processor state** required to
restart execution in an RTL simulation environment without performing
a full system boot.

