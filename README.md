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
```

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