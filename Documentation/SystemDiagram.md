## System Diagram
```mermaid
graph TD;
A[Powerbank] --Power--> B[Raspberry Pi 4]

B --display--> G[Laptop/Monitor]
B --OSC--> C[Reaper DAW]
B --USB MIDI--> D[Launchpad Pro MK3]

C --L-ISA Audio Bridge--> E[L-ISA Processor]
C --MIDI timecode--> I[GrandMA3]

D --USB MIDI--> B

E --Spatial Metadata--> F[L-ISA Controller]

F --Spatial Metadata--> E
F --LAN DANTE--> H[Yamaha QL1]

H --LAN DANTE--> M[Amplifier]

I --DMX universe 1--> J[Digi Fan]
I --sACN--> L[Hanging Lights]

J --wireless DMX--> K[Smoke Machine]

M --> N[Speakers]
