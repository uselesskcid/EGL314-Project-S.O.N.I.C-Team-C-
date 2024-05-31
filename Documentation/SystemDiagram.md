## System Diagram
```mermaid
graph TD;
A[Powerbank] --Power--> B[Raspberry Pi 4]
B --display--> G[Laptop/Monitor]
B --OSC--> C[Reaper DAW]
B --MIDI--> D[Launchpad Pro MK3]
C --L-ISA Audio Bridge--> E[L-ISA Processor]
C --MIDI timecode--> G[GrandMA3]
D --MIDI--> B
E --Special Metadata--> F[L-ISA Controller]
F --Special Metadata--> E
F --D/A--> H[Speakers]
G --DMX universe 1--> H[Digi Fan]
H --wireless dmx Tx & Rx--> [Smoke Machine]
