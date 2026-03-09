

# Capturing Architectural State with GDB

To analyze the processor state during early boot, QEMU can be
executed in debug mode and inspected using GDB.

## Starting QEMU in Debug Mode

Example command:

qemu-system-riscv64 \
 -machine virt \
 -nographic \
 -kernel Image \
 -S -s

The `-S` flag pauses execution at startup, and `-s` opens a GDB
debugging port.

## Connecting GDB

Run:

gdb-multiarch

Then connect to QEMU:

target remote :1234

## Inspecting Registers

To display all registers:

info registers

To inspect specific CSRs:

p/x $mstatus  
p/x $satp  
p/x $medeleg  
p/x $mideleg  

## Observing Boot State

During early boot, several observations can be made:

- `satp` is typically 0 before virtual memory is enabled
- `mstatus` controls privilege mode behavior
- trap delegation registers determine interrupt handling

These observations help identify the minimal architectural state
required for checkpointing.
