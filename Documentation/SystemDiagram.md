## System Diagram
```mermaid
graph TD;
A[Powerbank] --Power--> B[Raspberry Pi 4]
B --> G[Laptop/Monitor]
B --OSC--> C[Reaper DAW]
B --> D[Launchpad Pro MK3]
C --L-ISA Audio Bridge--> E[L-ISA Processor]
D-->B
E --Special Metadata--> F[L-ISA Controller]
F --Special Metadata--> E
