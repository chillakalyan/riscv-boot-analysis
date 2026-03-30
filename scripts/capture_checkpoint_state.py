
import subprocess

def capture_checkpoint_state():

    gdb_commands = """
target remote :1234
info registers
p/x $pc
p/x $mstatus
p/x $satp
p/x $mtvec
p/x $mepc
p/x $medeleg
p/x $mideleg
quit
"""

    with open("checkpoint_state.gdb", "w") as f:
        f.write(gdb_commands)

    subprocess.run(["gdb-multiarch", "-x", "checkpoint_state.gdb"])


if __name__ == "__main__":
    capture_checkpoint_state()
