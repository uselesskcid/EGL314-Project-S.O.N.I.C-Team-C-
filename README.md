<h1 align="center">
  Project S.O.N.I.C:
  <br>Station 5 – Memory Sequence
</h1>

<p align="center">
  <i align="center">Test and train your auditory memory with the use of modern technologies! 🥷</i>
</p>

<p align="center">
  <a href="https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C/commits/main/"><img src="https://img.shields.io/github/last-commit/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC.svg?style=for-the-badge"/></a>
</p>

## Table Of Contents 📚

<b>

- [Overview](#overview) 📃
- [About](#about) ⓘ
- [Directory](#directory) 🗂️
- [System Diagram](#sys-diag) 📔
- [Contributors](#contributors) 👥
- [Credits](#credits) 🙏

</b>

## <a id="overview"> Overview 📃</a>

Project S.O.N.I.C (Sensory Observation Ninja Immersive Challenge) is an experiential/exploratory initiative designed to blend the ancient "ninja training techniques" with modern technologies.

Students are to design a range of interactive stations that simulate ninja training scenarios, designed to test and enhance your listening abilities, reaction times and strategic thinking. The stations include:
1. Stealth Walking
2. The Blindfold Challenge
3. Art Of Hearing
4. Reaction Training
5. **Memory Sequence** (Team C)

<p>
This repository will focus strictly on the fifth station, the Memory Sequence.
</p>

## <a id="about"> About ⓘ </a>
The Memory Sequence tests and trains your auditory memory.
Participants are to listen, remember, and replicate complex sequences of sounds.

Player to interact with a 360° customized touchpad to indicate the memory sequence.

Only one player interacting with MIDI Launchpad Pro MK3 (360° customized touchpad).

<details open>
<summary>
  Features
</summary>
<ul>
  <li>L-ISA to create distinct sequences of sounds that vary in parameters (e.g. localizations, frequencies, etc) </li>
  <li>Adjustable difficulties where sequences increase in complexity</li>
  <li> Interactive Feedback – players will be blasted with smoke if they lose </li>
</ul>
</details>

## <a id="directory"> Directory 🗂️</a>

### 💯 ☑️ ▶️ [Full Documentation](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Final_Presentation/FinalPresentation.md)  ◀️ ☑️ 💯

For a proper and thorough walkthrough of our station, please click the link above. All codes, assets, pictures, guides, and in-depth explanations can be found there. This fully reflects our final piece of work in its concluded form.


### Legacy
Previous attempts at documentation can be found [here]() (Proof of Concept) and [here](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/MVP/MVP.md) (Minimum Viable Product). Both versions are deliberately left incomplete and visible to showcase our progress since.
<!-- Change this?? --->

## <a id="sys-diag"> System Diagram 📔</a>
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

## <a id="contributors"> Contributors 👥</a>
[//]: contributor-faces

### Team Members:<br>
<a href="https://github.com/uselesskcid"><img src="https://avatars.githubusercontent.com/u/123967722?v=4" title="uselesskcid" width="50" height="50"><strong> Dick (Team Leader)</strong></a><br>
<a href="https://github.com/ihave10minutes"><img src="https://avatars.githubusercontent.com/u/167286782?v=4" title="ihave10minutes" width="50" height="50"><strong> Lennon (Co-Lead)</strong></a><br>
<a href="https://github.com/Robloxer9000"><img src="https://avatars.githubusercontent.com/u/167287547?v=4" title="Robloxer9000" width="50" height="50"><strong> Quan Feng (Member)</strong></a><br>
<br>

### Open Source Contributors:<br>
<a href="https://github.com/tl0wh"><img src="https://avatars.githubusercontent.com/u/169418560?v=4=4" title="tl0wh" width="50" height="50"><strong> Travis (Classmate)</strong></a><br>

## <a id="credits"> Credits 🙏</a> 
Our team would like to specially thank:

<a href="https://github.com/ywfumav" title="ywfumav"><strong>Mr. Fu YongWei</strong></a> from **Nanyang Polytechnic** for overseeing our project phase and supplying us with base-source codes.

<a href="https://github.com/huats-club"><strong>Huats Club</strong></a> for many references in our installation.