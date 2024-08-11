<h1 align="center">
L-ISA Controller
</h1>

<p align="center">
  <i align="center">
  Rundown of L-ISA Controller related files
  </i>
</p>

## Table Of Contents 📚

<b>

- [Overview](#overview) 📃
- [Files In Use](#files-in-use) 📂
- [L-ISA Snapshots](#lisa-snapshots) 📷

</b>

## <a id="overview"> Overview 📃</a>

L-ISA Controller is a desktop spatial object mixing audio processing tool for operating multichannel audio output with L-ISA Processors.

In our game, it is used for audio effects such as our sound cues appearing from the front, back, left, and right side.

L-ISA Controller uses spatial metadata from L-ISA Processor (MTC timecode sync through MIDI with Reaper DAW).

## <a id="files-in-use"> Files In Use 📂</a>

📄 - [Master L-ISA Controller file](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/tree/main/MVP/L-ISA_Controller/MAINFILE_POC_FINAL.lisa)

This the the L-ISA Controller file that runs on the Master Station Laptop. It contains not just the audio effects and soundscape creation for our station, but other stations as well.

## <a id="lisa-snapshots"> L-ISA Snapshots </a> 📷

For reference, the picture below shows the snapshots with the MIDI timecode time that our team used.

![](Assets/TeamC_L-ISA_Controller.png)

In our game, many snapshots have the effect of the sound "rotating around" the player (i.e. the sound of a bird flapping, moving from east to west), which greatly give an immersive auditory experience if your eyes were closed.

This also gives us the ability to position our sound cue the player should listen out for (the shuriken) to be heard from the left, right, front or back. Without L-ISA, we would be limited to panning left and right only.
