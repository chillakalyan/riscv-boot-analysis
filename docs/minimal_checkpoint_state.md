# Minimal Checkpoint State

In order to restart execution in an RTL simulation environment without
repeating the entire boot sequence, a minimal architectural checkpoint
state must be captured.

The checkpoint should contain the minimum processor state necessary
to restore deterministic execution.

## Core Processor State

### Program Counter

The Program Counter (PC) contains the address of the next instruction
to be executed. Restoring the correct PC value is essential for
continuing execution from the checkpoint.

### General Purpose Registers

RISC-V provides 32 general-purpose registers:

x0 – x31

These registers contain intermediate computational state and must be
restored to preserve program correctness.

## Critical Control and Status Registers (CSRs)

Several CSRs define the execution context of the processor.

Important CSRs include:

- **mstatus** – Machine status register controlling privilege behavior
- **satp** – Supervisor address translation and protection register
- **mtvec** – Machine trap vector base address
- **mepc** – Machine exception program counter
- **medeleg** – Machine exception delegation register
- **mideleg** – Machine interrupt delegation register

These registers determine privilege mode transitions, interrupt
handling, and memory translation.

## Privilege Mode

The current processor privilege level must be restored correctly:

- Machine Mode (M)
- Supervisor Mode (S)

In most cases, the Linux kernel runs in Supervisor Mode after OpenSBI
initialization.

## Memory Context

If virtual memory is enabled, the page tables referenced by the `satp`
register must also be restored.

## Summary

A minimal checkpoint state may include:

- Program Counter (PC)
- General purpose registers (x0–x31)
- Key CSRs (mstatus, satp, mtvec, mepc, medeleg, mideleg)
- Current privilege mode
- Relevant memory state

Identifying the minimal state required allows faster restart of
execution in RTL simulations such as OpenPiton.
