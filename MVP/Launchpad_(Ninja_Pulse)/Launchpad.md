<h1 align="center">
Memory Sequence: Game Controller
</h1>

<p align="center">
<i align="center">Touch-based gamepad using Novation's Launchpad Pro MK3 </i>
</p>









## Overview
For the **Memory Sequence** game portion of Project S.O.N.I.C, we will be using the ***Launchpad Pro MK3*** as our MIDI touchpad. The game pad will be accomodating 2 of our essential gamemodes: easy and hard. The player will be able to play using the central LED buttons on the Launchpad and switch between easy and hard mode. They are also allowed to hear the audio sequence when pressing the "Start Sequence" button to look out for the correct answer. Once the audio marker has ended, they will press the submit button on the Launchpad to input their answers.










# Gameplay






You are greeted with a single start buttton on the Launchpad.
 
 After the start button is pressed, the layout of the starting game mode will appear to signify the start of game. 
 


<h1 align="center">
Memory Sequence: Game Controller
</h1>

<p align="center">
<i align="center">Touch-based gamepad using Novation's Launchpad Pro MK3 </i>
</p>









## Overview
For the **Memory Sequence** game portion of Project S.O.N.I.C, we will be using the ***Launchpad Pro MK3*** as our MIDI touchpad. The game pad will be accomodating 2 of our essential gamemodes: easy and hard. The player will be able to play using the central LED buttons on the Launchpad and switch between easy and hard mode. They are also allowed to hear the audio sequence when pressing the "Start Sequence" button to look out for the correct answer. Once the audio marker has ended, they will press the submit button on the Launchpad to input their answers.










# Gameplay






You are greeted with a single start buttton on the Launchpad.
 
 After the start button is pressed, the layout of the starting game mode will appear to signify the start of game. 
 






 
 ### Easy mode 
 
 ![](launchpad_assets/Launchpad_Easy.jpg)



 >The easy mode consists of the most basic directions: Left and Right.
 ### Hard mode 

 ![](launchpad_assets/Launchpad_Hard.jpg)
 >The hard mode consists of four directions: North, South, East and West, with the playable buttons being inside the white circle.

During each game mode, Players have to look out for audio cues and memorize the order of directions of the sound. 
- Inside the moving pixels are the direction inputs. The middle grey pixel represents the player's position

- On the bottom left corner lies the audio sequence play button. Once pressed, all inputs will be blocked temporarily.

-  After the audio sequence is finished, the player will be able to input their answers.

- The player must press the yellow submit button on the right side of the Launchpad to see whether they have inputted the correct answer. 


## Development












We made 3 ```python``` files: one for easymode, one for hard mode and then another one for the main code that we will be using to run the overall code to operate our whole game.

- Main file:

- Easy mode file: 

- Hard mode file: 

For all three files, we need to start off by making sure that the Raspberry Pi is able to communicate with the Raspberry Pi through MIDI.


First we need to import the mido library.
```
import mido
```
 -  The "mido" library stores most of the functions that we will be coding for our game to function.

Then, you will need create two variables and each variable opens the input port and output port for recieving MIDI messages and sending MIDI commands respectively.

```

# Example:

outport = mido.open_output('Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0')
inport = mido.open_input('Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0')
```
>  - "outport" and "inport" are variables.
>  - "mido.open_output" and "mido.open_input" are both functions from the mido library.
> - Both the mido functions state the names for the input port and output ports of the Launchpad (Both are named ***'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'***) in order to open these ports for Launchpad and Raspberry Pi MIDI communication.

### Adding colours (All files)

To add colour to the LEDs, we would need to assign a colour code to the ID number of the LEDs. To find out the colour codes of the Launchpad, refer to the [Launchpad Pro Programmer's Manual.]((https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/downloads/LPP3_prog_ref_guide_200415.pdf))

We need to start off by sending this output message to the Launchpad in order to tell it to light up 1 LED with a desired colour.
```

# Example 
def pixel(buttonid, colour):
     outport.send(mido.Message('note_on', note=buttonid, velocity=colour))
```
> - The output port sends a MIDI message to the Launchpad.  'note_on' tells the LED to light up.
> - For the Launchpad, 'note' is referred to as the button ID of an LED, and 'velocity' is referred to the colour of the LED to light up.
> - 'pixel(buttonid, colour)' is defined as a function to light up 1 LED with a specific colour.



After which you can start colouring your buttons. For example, if I want to colour 2 LEDs of my choice:
```
# Example:

def light_mode_buttons():
    led(17, 64)       # Colour (green)
    led(18, 72)       # Colour (red)
```

> - The numbers **17** and **18** represent the ID numbers of the two LED buttons.
> - The number **64** is the colour code for green, while the colour for red is **72**.

### Button feedback (All files)

We can also receive input feedback on our Raspberry Pi when pressing the LEDs on the Launchpad as they can also act as buttons for sending messages to the Raspberry Pi.
When pressing a button
- a message on the Rasberry Pi terminal is shown
- audio/ lighting sequences implemented into the code will play


### Main file

The code file that we will only be running on our Raspberry Pi terminal is our **main file** whch is the master file that sets up the whole game and  controls the running process of each individual game mode. 
 - The orange start button is coded inside the main file to start and load the whole game on the Launchpad.

 - The functions of the two difficulty mode buttons are coded in the main file to switch between easy and hard mode. This means that the main file can load the easy or hard mode depending on which difficulty mode button the player presses.



- More modules are imported in this file such as ```time```, ```subprocess``` and ```threading``` in order to create functions to run one difficulty mode at a time.




### Easy mode file
The layout for easy mode shows up when this file is loaded. 
- Players can input the directions "Left" and "Right" with the input buttons.
- The code contains the design layout for Easy mode on the Launchpad. 
- The easy sequence play button on **Button ID 11** is coded with a function to play the easy mode audio sequence.
- Submit button on **Button ID 38** to submit the player's answers.



### Hard mode file
The layout for hard mode shows up when this file is loaded. 
- Players can input the directions "North", "South", "East" and "West" with the input buttons.
- The code contains the design layout for Hard mode on the Launchpad. 
- The easy sequence play button on **Button ID 12** is coded with a function to play the Hard mode audio sequence.
- Submit button on **Button ID 48** to submit the player's answers.

### Button feedback (All files)

We can also receive input feedback on our Raspberry Pi when pressing the LEDs on the Launchpad as they can also act as buttons for sending messages to the Raspberry Pi.

When pressing a button:
- a message on the Rasberry Pi terminal is shown
- audio/ lighting sequences implemented into the code will play

In addition, when players press the input buttons:
-  The colour of the input buttons change colour to white when pressed
-  The button reverts back to its original supposed colour when let go

Generally when a button is pressed, the colour of the button blinks.
This is implemented to improve the user feedback.