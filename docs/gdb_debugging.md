# Debugging RISC-V Boot with GDB

QEMU provides debugging support that allows inspection of the processor
state using GDB.

This is useful for analyzing register values and architectural state
during the early boot process.

## Starting QEMU in Debug Mode

Example command:
```
qemu-system-riscv64 \
 -machine virt \
 -nographic \
 -kernel Image \
 -S -s
```
Explanation:

- `-S` pauses execution at startup
- `-s` opens a GDB debugging port (default port 1234)

## Connecting GDB

Start GDB:
```
gdb-multiarch
```
Connect to the QEMU target:
```
target remote :1234
```
## Inspecting Registers

Display all registers:
```
info registers
```
Inspect specific CSRs:
```
p/x $mstatus  
p/x $satp  
p/x $mtvec  
p/x $mepc  
p/x $medeleg  
p/x $mideleg  
```
## Observations

Using GDB allows us to observe the processor state at different points
during the boot sequence.

These observations are useful for identifying the minimal architectural
state required for checkpoint-based simulation.


