<h1 align="center">
  Project S.O.N.I.C - Activity 5 – Memory Sequence
</h1>

<p align="center">
  <i align="center">Test and train your auditory memory with the use of modern technologies 🥷</i>
</p>

<p align="center">
  <a href="https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C/commits/main/"><img src="https://img.shields.io/github/last-commit/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C.svg?style=for-the-badge"/></a>
</p>

## Overview
Project S.O.N.I.C (Sensory Observation Ninja Immersive Challenge) is an experiential/exploratory initiative designed to blend the ancient "ninja training techniques" with modern technologies. Students are to design a range of interactive stations that simulate ninja training scenarios, designed to test and enhance your listening abilities, reaction times and strategic thinking. The stations include:
1. Stealth Walking
2. The Blindfold Challenge
3. Art Of Hearing
4. Reaction Training
5. **Memory Sequence** (Team C)
6. Graduation Sequence
<p>
  In this repository, the focus will be strictly on Station 5 - Memory Sequence.
</p>

## Station 5 - Memory Sequence
“Memory Sequence” test and train your auditory memory.<br>
Participants are to listen, remember, and replicate complex sequences of sounds.<br>
Player to interact with a 360° customized touchpad to indicate the memory sequence.<br>
<br>
Only one Player interacting with MIDI Launchpad Pro MK3 (360° customized touchpad). <br>

<details open>
<summary>
  Features
</summary>
<ul>
  <li>L-ISA to create distinct sequences of sounds that vary in parameters (e.g. localizations, frequencies, etc) </li>
  <li>Adjustable difficulties where sequences can gradually increase in complexity (e.g. length, pitch, etc). </li>
  <li> Interactive Feedback – teams may consider integrating visual and tactile feedback as hints or penalties. </li>
</ul>
</details>

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
D <--universe 1 DMX--> M[Wireless DMX Tx]
M <--wireless--> N[Wireless DMX Rx]
N <--DMX--> P[G Force 2 Smoke Machine]
P <--DMX--> Q[Generic DMX Fan]

F <--Spatial MetaData--> G[L-ISA Controller]
G <--LAN Dante--> H[Mixer<br>Yamaha QL1]
H <--LAN Dante--> I[Amplifier<br>Yamaha XMV8140D]
I --Speaker Cable to Euroblock (4P)--> J[12 Speakers<br>Yamaha VXS5]
```

## Credits
Team C would like to specially thank, <a href="https://github.com/ywfumav" title="ywfumav"><strong>Mr. Fu YongWei</strong></a>   from **Nanyang Polytechnic** for overseeing our project phase and supplying us with base-source codes.

## Contributors to this Project:
[//]: contributor-faces
Team Members:<br>
<a href="https://github.com/uselesskcid"><img src="https://avatars.githubusercontent.com/u/123967722?v=4" title="uselesskcid" width="50" height="50"><strong> Dick (Team Leader)</strong></a><br>
<a href="https://github.com/ihave10minutes"><img src="https://avatars.githubusercontent.com/u/167286782?v=4" title="ihave10minutes" width="50" height="50"><strong> Lennon (Co-Lead)</strong></a><br>
<a href="https://github.com/Robloxer9000"><img src="https://avatars.githubusercontent.com/u/167287547?v=4" title="Robloxer9000" width="50" height="50"><strong> Quan Feng (Member)</strong></a><br>
<br>
<br>
Open Source Contributors:<br>
<a href="https://github.com/tl0wh"><img src="https://avatars.githubusercontent.com/u/169418560?v=4=4" title="tl0wh" width="50" height="50"><strong> Travis (Classmate)</strong></a><br>
