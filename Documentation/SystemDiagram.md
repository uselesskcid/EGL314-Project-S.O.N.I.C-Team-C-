## System Diagram
```mermaid
graph TD;
A[Powerbank] --Power--> B[Raspverry Pi 4]
B --> E[Laptop]
B --OSC--> C[Reaper DAW]
B --> D[Launchpad Pro MK3]
C --L-ISA Audio Bridge--> E[L-ISA Processor]
D-->B
E --Special Metadata--> F[L-ISA Controller]
F --Special Metadata--> E
