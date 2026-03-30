import subprocess
import os

"""
dump_registers.py

This script connects to a running QEMU instance using GDB and
extracts important architectural registers that may be required
for checkpoint-based execution restart.

Requirements:
- qemu-system-riscv64 running with: -S -s
- gdb-multiarch installed
"""

GDB_SCRIPT = """
target remote :1234

echo ===== GENERAL REGISTERS =====\\n
info registers

echo ===== IMPORTANT CSRs =====\\n
p/x $pc
p/x $mstatus
p/x $satp
p/x $mtvec
p/x $mepc
p/x $medeleg
p/x $mideleg

quit
"""

def create_gdb_script():
    """Create temporary GDB command file."""
    with open("dump_state.gdb", "w") as f:
        f.write(GDB_SCRIPT)

def run_gdb():
    """Run GDB with the generated script."""
    print("Connecting to QEMU via GDB...")
    subprocess.run(["gdb-multiarch", "-x", "dump_state.gdb"])

def cleanup():
    """Remove temporary script."""
    if os.path.exists("dump_state.gdb"):
        os.remove("dump_state.gdb")

def main():
    create_gdb_script()
    run_gdb()
    cleanup()

if __name__ == "__main__":
    main()
