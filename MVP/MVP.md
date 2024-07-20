<<h1 align="center">
  Minimum Viable Product
</h1>

<p align="center">
  <i align="center"> </i>a test of auditory Memory Sequence
</p>

## Overview
This repository folder contains all the notable assets, codes and others used for our Minimum Viable Product (MVP) in Week 14 that covers Station 5 - Memory Sequence.

In the Minimum Viable Product, we will be using a Master Station that is shared with the other teams. The Master Station hosts 3 different open-source softwares and they are Reaper DAW, L-ISA Controller and GrandMA3. There are 12 speakers in a 10 by 10 meters room and the participant will be standing in the center of the room to play their game.

For the Minimum Viable Product, the demonstration will feature a full run through of the game. This includes a introduction, 2 difficulty levels, followed by a win/lose sequence. There are 2 Graphical User Interface (GUI) used, one for the game and another for a laser sequence show displayed.

## Hardware & Software Setup
```mermaid
graph TD
A <--MIDI<br>USB 3.0 to USB C--> K[Launchpad Pro MK3<br>Customized Touchpad] 
A --display--> O[Laptop GUI]
A[Raspberry Pi 4 Master] <--LAN/WiFi + OSC --> B[Master Laptop]

B <--Running OSC--> C[Reaper DAW]
B <--Running OSC--> D[GrandMA3<br>Lighting Console]

C[Reaper<br>DAW] <--LAN Dante VSC --> F[L-ISA Processor]

D <--LAN sACN--> E[Hanging Lights<br>Ayrton Mistral, Magicblade, Minipanel<br>Showline ePar]
D <--universe 1 DMX--> M[Wireless DMX Tx]
M <--wireless--> N[Wireless DMX Rx]
N <--DMX--> P[G Force 2 Smoke Machine]
P <--DMX--> Q[Generic DMX Fan]

F <--Spatial MetaData--> G[L-ISA Controller]
G <--LAN Dante--> H[Mixer<br>Yamaha QL1]
H <--LAN Dante--> I[Amplifier<br>Yamaha XMV8140D]
I --Speaker Cable to Euroblock (4P)--> J[12 Speakers<br>Yamaha VXS5]

J[Laptop GUI] <--LAN/WiFi + OSC--> K[Raspberry Pi - Laser Master]
K -WiFi---> L[Raspberry Pi - Laser Slave 1]
K --WiFi--> M[Raspberry Pi - Laser Slave 2]
K --WiFi--> N[Raspberry Pi - Laser Slave 3]
K --WiFi--> O[Raspberry Pi - Laser Slave 4]
K --WiFi--> P[Raspberry Pi - Neopixel]