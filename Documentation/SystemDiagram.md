## System Diagram
```mermaid
graph TD;
A[Powerbank] --Power--> B[Raspberry Pi 4 (Master)]

B --OSC--> C[Raspberry Pi 4 (Slave)]
B --LAN/Wifi + OSC/MTC--> D[Master Laptop]

C --OSC--> B
C --LAN/Wifi + MIDI--> M[Laptop/Monitor]

D --Running OSC--> E[GrandMA3 Lighting Console]
D --Running MTC--> G[Reaper DAW]

E --sACN--> F[Hanging Lights<br> Ayrton Mistral, Magicblade, Minipanel, Showline ePar]
E --universe 1--> O[Smoke Machine<br> GeForce]

G --Dante VSC--> H[L-ISA Processor]

H --Dante VSC--> G
H --Spatial Metadata--> I[L-ISA Controller]

I --Spatial Metadata--> H
I --Dante LAN--> J[Audio Mixer<br> Yamaha QL1]

J --Dante LAN--> I
J --Dante LAN--> K[Amplifier<br> Yamaha XMV8140D]

K --Speaker Cable to Euroblock (4P)--> L[12x Speakers<br> Yamaha VXS5]

M --Running MIDI--> N[360° customized touchpad<br> Launchpad Pro MK3]

N --MIDI--> M

O --wireless DMX--> P[Smoke Machine]
```
