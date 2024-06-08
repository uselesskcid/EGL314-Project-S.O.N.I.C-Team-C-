## System Diagram:
```mermaid
graph TD
A <--MIDI<br>USB 3.0 to USB C--> K[Launchpad Pro MK3<br>Customized Touchpad] 
A --display--> O[Laptop]
A[Raspberry Pi 4 Master] <--LAN/WiFi + OSC --> B[Master Laptop]

B <--Running OSC--> C[Reaper DAW]
B <--Running OSC--> D[GrandMA3<br>Lighting Console]

C[Reaper<br>DAW] <--LAN Dante VSC --> F[L-ISA Processor]

D <--LAN sACN--> E[Hanging Lights<br>Ayrton Mistral, Magicblade, Minipanel<br>Showline ePar]
D <--universe 1--> M[Smoke Machine]
M <--Wireless DMX--> N[DMX Fan]

F <--Spatial MetaData--> G[L-ISA Controller]
G <--LAN Dante--> H[Mixer<br>Yamaha QL1]
H <--LAN Dante--> I[Amplifier<br>Yamaha XMV8140D]
I --Speaker Cable to Euroblock (4P)--> J[12 Speakers<br>Yamaha VXS5]
```
