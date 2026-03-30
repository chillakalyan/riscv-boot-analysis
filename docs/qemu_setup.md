# QEMU Setup for RISC-V Boot Analysi

This document describes how to run a RISC-V Linux system using QEMU and
OpenSBI firmware.

## Install Required Tools

Install QEMU and debugging tools:
```
sudo apt update
sudo apt install qemu-system-misc gdb-multiarch
```
## Download OpenSBI
```
git clone https://github.com/riscv-software-src/opensbi
```
## Running Linux in QEMU

Example command:
```
qemu-system-riscv64 \
 -machine virt \
 -m 2G \
 -nographic \
 -bios default \
 -kernel Image \
 -append "console=ttyS0"
```
## Debug Mode

To analyze the boot sequence using GDB:
```
qemu-system-riscv64 \
 -machine virt \
 -nographic \
 -kernel Image \
 -S -s
```
Then connecting with GDB:

Start GDB:
```
gdb-multiarch
```
Connect to the QEMU target:
```
target remote :1234
```
## Purpose

Running QEMU with debugging support allows inspection of processor
state during boot and helps identify the architectural state required
for checkpoint-based simulation.
