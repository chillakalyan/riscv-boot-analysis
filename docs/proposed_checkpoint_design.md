Goa
```
Design a minimal checkpoint mechanism for RISC-V RTL simulation
```

Checkpoint Capture Point
```
After Linux reaches stable state
```

Minimal State (your hypothesis)
```
• PC
• x0–x31
• mstatus
• satp
• mtvec
• mepc
• medeleg / mideleg
```

Checkpoint Flow
```
Capture → Serialize → Store → Restore → Resume
```

Challenges
```
• memory consistency
• device state
• determinism
```

Future Work
```
Integration with OpenPiton
```
