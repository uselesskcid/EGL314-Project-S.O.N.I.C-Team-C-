

<h1 align="center">
Memory Sequence: Game Controller
</h1>

<p align="center">
<i align="center">Touch-based gamepad using Novation's Launchpad Pro MK3 </i>
</p>









## Overview
For the **Memory Sequence** game portion of Project S.O.N.I.C, we will be using the ***Launchpad Pro MK3*** as our MIDI touchpad. The game pad will be accomodating 2 of our essential gamemodes: easy and hard. The player will be able to play using the central buttons on the Launchpad and switch between easy 






# Getting started


We will be connecting our ***Launchpad*** to our ***Rasberry Pi 4*** with a ***USB-C to USB-A cable*** through their respective ports. After which we will be coding on the Raspberry Pi using ```Python```. 

Several things to note before proceeding:

-  Ensure that your Raspberry Pi is updated. (e.g date and time, etc) 

-  Make sure you are running a virtual environment (Create if you do not have one, refer to [here](https://github.com/huats-club/mts_sensor_cookbook/blob/main/0.%20virtual_environment/venv.md) for more details)

-  Make sure that you have **python-osc** downloaded in your virtual environment.

> You should now be running your virtual environment on your Raspberry Pi terminal.


Now, install the following module inside your virtual environment:





     
    pip install mido
     
  After you have installed the module, you can proceed to check the **input and outport ports** of your Launchpad. We will need the **MIDI input port** in order to get our code to run from our Raspberry Pi to our Launchpad.  
       
     
   Connect your Launchpad to your Rasberry Pi first using your USB-C to USB-A cable, then put in the following code on a python file and run it on your virtual environment:
   ```
import mido

# List all inpuport midot MIDI devices
    print("Input MIDI Devices:")
    for input_name in mido.get_input_names():
    print(input_name)

# List all output MIDI devices
    print("\nOutput MIDI Devices:")
    for output_name in mido.get_output_names():
    print(output_name)

     
  ```
     
You would then be able to see three input ports from your Launchpad. Note down the one with the MIDI input port.
     
Then, we will need to find the ID number for each LED on the Launchpad to start configuring our buttons as well as assigning colours to each LED on the Launchpad. 


![ALT TEXT](./assets/buttonids.png) 

>- On the central area of your Launchpad, there is an 8x8 LED layout in which the LEDS can be controlled with their respective numerical ID numbers. You will need to use those ID numbers inside your code in order to configure your LED lights and buttons.     

You can choose to refer to the [Launchpad Pro MK3's Programmer's manual](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/downloads/LPP3_prog_ref_guide_200415.pdf), or you can follow the tutorial on [huats-club.](https://github.com/huats-club/mts_sensor_cookbook/blob/main/4.%20midi/midi.md)


### Starting your Launchpad
Activate your Launchpad's **Custom Mode 8**. This is where our game will be played with the touch LED buttons. 

**Hit the "Custom" button and then the 8th bottom button on the far right.**
![ALT TEXT](./assets/launchpadpromk3pad.jpg) 









 

 ***If you want to reset your LED lights/buttons, switch to another custom mode then come back to custom mode 8. The LED lights of the touch buttons will disappear.***




# Gameplay Development

## Our Gamepad




You are greeted with a single start buttton on the Launchpad.
 
 After the start button is pressed, the layout of the starting game mode will appear to signify the start of game. 
 
 On the bottom right hand corner,
 there are two buttons to switch between difficulty modes with green loading the easy mode and red loading the hard mode.





 
 ### Easy mode (Green)
 
 ![alttext](./assets/easymode.jpeg)



 >The easy mode consists of the most basic directions: Left and Right.
 ### Hard mode (Red)

 ![alttext](./assets/hardmode.jpeg)
 >The hard mode consists of four directions: North, South, East and West, with the playable buttons being inside the white circle.

For each game mode, the layout represents the environment in which the player has to me
- The environment has different groups of speakers representing different directions of sound.
- The playable buttons surrounding the player's position
- The white button on the center of the layout represents the player's position.
- The colored LEDs that are outside the white space represent the speakres, according to which direction they are from.



## How the code works


We made 3 ```python``` files: one for easymode, one for hard mode and then another one for the main code that we will be using to run the overall code to operate our whole game.

- Main file : **[main_file.py](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Launchpad%20Pro............../main_file.py)**

- Easy mode file: **[easymode_june5.py](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC)**

- Hard mode file: **[hardmode_june5.py](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Launchpad%20Pro/hardmode_june5.py)**

For all three files, we need to start off by making sure that the Raspberry Pi is can communicate with the Raspberry Pi through MIDI.

First we need to import the mido library.
```
import mido
```
 -  The "mido" library stores most of the functions that we will be coding for our game to function.

Then, you will need create two variables and each variable opens the input port and output port for recieving MIDI messages and sending MIDI commands respectively.

```

# Example:

outputport = mido.open_output('Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0')
inputport = mido.open_input('Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0')
```
>  - "outputport" and "inputport" are variables.
>  - "mido.open_output" and "mido.open_input" are both functions from the mido library.
> - Both the mido functions state the names for the input port and output ports of the Launchpad (Both are named ***'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'***) in order to open these ports for Launchpad and Raspberry Pi MIDI communication.

### Main file

The code file that we will only be running on our Raspberry Pi terminal is our main file ([main_file.py](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Launchpad%20Pro............../main_file.py)) whch is the master file that sets up the whole game and  controls the running process of each individual game mode. 
 - The start button is coded inside the main file to run whole game on the Launchpad.
 - The two difficulty mode buttons are coded in the main file to switch between easy and hard mode. This means that the main file can load both the easy and hard mode ```python``` code files depending on which button the player presses.

- The files for easy mode() and hard mode() consists of colouring code for the LEDs to implement their respective layout designs. 
> - User button feedback is implemented


 

In our ```Python``` codes, we assign colours to the LEDs on our Launchpad for the overall layout design including the functional buttons. 

- For both easy and hard mode, we assigned colours for the buttons and 


test