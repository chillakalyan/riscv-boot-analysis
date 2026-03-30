
# OpenSBI → Linux Boot Transitio

In a RISC-V system using OpenSBI firmware, the processor begins
execution in Machine Mode (M-mode). OpenSBI performs platform
initialization and then transfers control to the operating system.

## Boot Sequence Overview
```
CPU Reset
↓
OpenSBI firmware (Machine Mode)
↓
CSR initialization
↓
Trap delegation
↓
Switch to Supervisor Mode
↓
Linux kernel entry
```
## Machine Mode Initialization

OpenSBI configures several important machine-level registers:
```
- mstatus
- mtvec
- medeleg
- mideleg
```
These registers control interrupt handling and exception delegation.

## Trap Delegation

OpenSBI configures the following registers:
```
- **medeleg** – delegates exceptions to Supervisor Mode
- **mideleg** – delegates interrupts to Supervisor Mode
```
This allows Linux to handle most traps directly.

## Transition to Supervisor Mode

After initialization, OpenSBI performs a controlled transition to
Supervisor Mode by setting the appropriate CSR values and jumping
to the kernel entry point.

The Linux kernel then begins execution in S-mode.

## Importance for Checkpointing

Understanding the OpenSBI → Linux transition is important when
determining the minimal architectural state required to restore
execution from a checkpoint.

Key registers modified during this transition must be included
in the checkpoint state.
