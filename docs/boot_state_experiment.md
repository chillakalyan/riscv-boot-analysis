# Experiment: Capturing Architectural State During Boot

This experiment captures the architectural processor state during the
early boot sequence of a RISC-V Linux system running in QEMU with
OpenSBI firmware.

The goal is to observe how processor state evolves during the boot
process and identify the minimal state required for checkpointing.

## Setup

The system was executed using QEMU with the following configuration:

- QEMU RISC-V virt machine
- OpenSBI firmware
- Linux kernel (RISC-V)
- gdb-multiarch for debugging

QEMU was launched in debug mode:

qemu-system-riscv64 \
 -machine virt \
 -nographic \
 -kernel Image \
 -S -s

GDB was then attached to the running system.

## Captured Architectural State

Example architectural state observed during early boot:

pc       = 0x8000b64a  
satp     = 0x0  
mstatus  = 0xa00000000  
medeleg  = 0x0  
mideleg  = 0x1444  

## Observations

satp = 0  
Virtual memory is not yet enabled during early boot.

mstatus = 0xa00000000  
Indicates machine mode configuration before transitioning to
supervisor mode.

medeleg / mideleg  
Trap delegation registers define which exceptions and interrupts
will be handled by supervisor mode.

## Relevance to Checkpointing

Capturing this architectural state allows the simulator to restore
execution without repeating the entire boot sequence.

This approach can significantly reduce simulation time in RTL
platforms such as OpenPiton.
