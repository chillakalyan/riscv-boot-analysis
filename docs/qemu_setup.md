\# QEMU RISC-V Setup



Install required tools:



sudo apt update

sudo apt install qemu-system-misc gdb-multiarch



Download OpenSBI:



git clone https://github.com/riscv-software-src/opensbi



Boot Linux using QEMU:



qemu-system-riscv64 \\

&nbsp;-machine virt \\

&nbsp;-m 2G \\

&nbsp;-nographic \\

&nbsp;-bios default \\

&nbsp;-kernel Image \\

&nbsp;-initrd rootfs.cpio \\

&nbsp;-append "console=ttyS0"

