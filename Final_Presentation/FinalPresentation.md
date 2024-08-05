<h1 align="center">
  Final Presentation
</h1>

<p align="center">
  <i align="center">A rundown of our station, delivered on our Final Presentation
  </i>
</p>

### Table Of Contents 📚

- [Overview](#overview) 📃
- [Getting Started!](#getting-started) 🔛
- [Hardware & Software Setup](#setup) ⚙️

## <a id="overview"> Overview 📃</a>
This repository folder contains all the notable assets, codes and others used for our Final Production in Week 17 that covers our station - Memory Sequence.

In the Minimum Viable Product, we will be using a Master Station shared with others. The Master Station hosts 3 different open-source softwares, which are Reaper, L-ISA Controller and GrandMA3. Besides software, there are 12 speakers in a 10 by 10 meters room shared as well.

The final demonstration will feature a full run through of our station. This includes an introduction, 2 difficulty levels, followed by a win/lose sequence. Once the game ends, we are to segway into our laser show as a wrap up. 


## <a id="getting-started"> Getting Started 🔛</a>
### Installation Guide

1️⃣ Your first stop! [Take a gander](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/Documentation/Installation_Guide.md) as to how we installed everything, as well as how you can do it too.

### Software & Hardware Overview

🔳 Sound effects in our levels are ran through <b>Reaper.</b> [Dive deeper](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/Reaper_DAW/Reaper.md) into the behind-the-scenes of our level creations.

🔳 <b>L-ISA's</b> spatial object mixing takes our gameplay one step higher. [Go in-depth](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/L-ISA_Controller/L-ISA.md) into the specifics of what goes on.

🔳 <b>grandMA3</b> provides a lighting control platform for our station. [Watch]((https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/GrandMA3/grandma3.md)) as our work comes to light.

🔳 Our softwares used are operated by <b>PythonOSC.</b> [See how](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/OSC/OSC.md) a humble laptop can control our entire system.

🔳 We had the privilege of using a <b>Launchpad</b> for our gameplay. [Dig into](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/Launchpad_(Ninja_Pulse)/Launchpad.md) how we utilised its power.

🔳 Besides gameplay, we contributed to a remarkable <b>laser show</b>. [Take a look](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/Laser_Sequence/Laser.md) at the flashy lights and their set-up.

### Slides
Many groups use a poster. We went for [a slightly different approach](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/Slides).

## <a id="setup"> Hardware & Software Setup ⚙️</a>
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

R[Laptop GUI] <--LAN/WiFi + OSC--> S[Raspberry Pi - Laser Master]
S <--LAN/WiFi + OSC --> B
S <--WiFi + OSC---> T[Raspberry Pi - Laser Slave 1]
S <--WiFi + OSC--> U[Raspberry Pi - Laser Slave 2]
S <--WiFi + OSC--> V[Raspberry Pi - Laser Slave 3]
S <--WiFi + OSC--> W[Raspberry Pi - Laser Slave 4]
S <--WiFi + OSC--> X[Raspberry Pi - Neopixel]

T --Relay Module--> Y[Laser Modules - 6 for each Raspberry Pi]
U --Relay Module--> Y
V --Relay Module--> Y
W --Relay Module--> Y
X --Dupont(F)<-> XLR(F) to XLR(M) to Dupont(M)(Soldered)--> Z[Neo Pixel LED Strip]
```