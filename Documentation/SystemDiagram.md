## System Diagram
```mermaid
graph TD;
A[Powerbank] --Power--> B[Raspberry Pi 4]

B --display--> G[Laptop/Monitor]
B --OSC--> C[Reaper DAW]
B --MIDI--> D[Launchpad Pro MK3]

C --L-ISA Audio Bridge--> E[L-ISA Processor]
C --MIDI timecode--> I[GrandMA3]

D --MIDI--> B

E --Special Metadata--> F[L-ISA Controller]

F --Special Metadata--> E
F --D/A--> H[Speakers]

I --DMX universe 1--> J[Digi Fan]
I --DMX universe 2--> L[Hanging Lights]

J --wireless dmx Tx & Rx--> K[Smoke Machine]
