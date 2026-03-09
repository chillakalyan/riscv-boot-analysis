# CSR Analysis During Boot

Control and Status Registers (CSRs) play a critical role in the
RISC-V privilege architecture.

During the early boot process, several CSRs are configured by OpenSBI
before transferring control to the Linux kernel.

## Key CSRs Observed

### mstatus

The **mstatus register** controls machine-level privilege behavior.

It defines:

- interrupt enable bits
- privilege transitions
- execution mode configuration

### satp

The **satp register** controls address translation and virtual memory.

Fields include:

- MODE – translation mode
- ASID – address space identifier
- PPN – page table base address

During early boot, `satp` is often zero because virtual memory has not
yet been enabled.

### mtvec

The **mtvec register** stores the base address of the machine trap
handler.

This register determines where the processor jumps when an exception
or interrupt occurs in Machine Mode.

### mepc

The **mepc register** stores the program counter at the time of an
exception in Machine Mode.

It is used to resume execution after handling the exception.

### medeleg / mideleg

These registers determine which exceptions and interrupts are delegated
to Supervisor Mode.

This allows the Linux kernel to manage traps directly.

## Importance

Analyzing these CSRs helps determine:

- processor execution context
- privilege mode transitions
- minimal state required for checkpoint recovery
