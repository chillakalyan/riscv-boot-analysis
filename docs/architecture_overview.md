
# RISC-V Architecture Overvie

RISC-V is an open instruction set architecture designed for
modularity and extensibility.

## Privilege Levels

RISC-V defines multiple privilege levels:
```
- Machine Mode (M) – highest privilege
- Supervisor Mode (S) – operating system
- User Mode (U) – user applications
```
Machine Mode is responsible for low-level system initialization.

## Control and Status Registers

CSRs control processor configuration, trap handling,
and memory management.

Important examples:
```
- mstatus
- mtvec
- mepc
- satp
```
## Firmware and Boot Process

In many systems, OpenSBI acts as firmware that initializes the
machine and prepares the system for the operating system.

OpenSBI runs in Machine Mode and transfers control to the
Linux kernel in Supervisor Mode.

## Relevance to This Project

Understanding the architecture and privilege transitions is
essential for identifying the minimal processor state required
for checkpoint-based simulation.
