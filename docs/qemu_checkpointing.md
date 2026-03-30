# QEMU Checkpointing and Snapshot Mechanisms

QEMU provides several mechanisms for saving and restoring the state
of a virtual machine. These mechanisms are closely related to the
concept of checkpointing required for restarting execution without
performing a full system boot.

## VM Snapshots

QEMU supports snapshots which allow saving the complete virtual
machine state at a given point in time.

Commands available in the QEMU monitor include:
```
savevm <tag>
loadvm <tag>
```
These commands save and restore the following:

- CPU register state
- memory contents
- device state
- virtual machine configuration

Snapshots allow the system to resume execution from the saved point.

## Migration Mechanism

QEMU also supports live migration, which transfers the full VM state
from one host to another.

Migration internally captures:
```
- CPU state
- RAM state
- device state
```
This mechanism is implemented using the **VMState** framework in QEMU.

## Relevance to Checkpointing

Checkpointing in RTL simulation environments such as OpenPiton may
require capturing a similar set of state information:
```
- CPU architectural state
- memory contents
- device state (if necessary)
```
Studying how QEMU performs VM state capture can help determine which
components of the processor state must be saved in order to resume
execution deterministically.

## References

QEMU Migration Documentation  
https://www.qemu.org/docs/master/devel/migration.html
