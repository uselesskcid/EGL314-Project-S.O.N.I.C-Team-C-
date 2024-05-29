## System Diagram
```mermaid
graph TD;
A[Powerbank]-Power->B[Raspverry Pi 4]
B[Raspberry Pi 4]-OSC->C[Reaper DAW]
B-->D[Launchpad Pro MK3]
C-->B
D-->B