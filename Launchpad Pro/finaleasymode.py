import mido

# Set up Launchpad MIDI ports for input and output
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # Output port for sending commands to Launchpad
inport = mido.open_input(midipad)  # Input port for receiving feedback from Launchpad

# Dictionary to store original colors for each button
ogcolour = {
    64: 10,  # Colors for NORTH
    83: 10,  
    84: 10, 
    85: 10,
    44: 4,   # Colors for SOUTH
    23: 4,
    24: 4,
    25: 4,   
    55: 40,  # Colors for EAST
    57: 40,
    47: 40,
    67: 40,
    53: 30,  # Colors for WEST
    51: 30,
    41: 30,
    61: 30
}

# Function to set the color of a specific button
def pixel(buttonid, colour):
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)  # Output command to Launchpad

# Function to initialize the buttons with their original colors
def initialize_buttons():
    # Set initial color for NORTH button and associated row
    pixel(64, ogcolour[64])
    for i in range(83, 86):
        pixel(i, ogcolour[i])
    # Set initial colors for other buttons and rows/columns
    buttonnorth(10)
    buttonsouth(4)
    buttonwest(30)
    buttoneast(40)
    middlebutton(3)
    nfill(10)
    sfill(4)
    wfill(30)
    etfill(40)
    box(3)

# Individual button functions to set their colors
def buttonnorth(nbutton):
    pixel(64, nbutton)

def buttonsouth(sbutton):
    pixel(44, sbutton)

def buttonwest(wbutton):
    pixel(53, wbutton)

def buttoneast(ebutton):
    pixel(55, ebutton)

def middlebutton(mbutton):
    pixel(54, mbutton)

# Functions to fill rows or columns with a specific color
def nfill(north):
    for i in range(83, 86):
        pixel(i, north)

def sfill(south):
    for i in range(23, 26):
        pixel(i, south)

def wfill(west):
    pixel(41, west)
    pixel(51, west)
    pixel(61, west)

def etfill(east):
    pixel(47, east)
    pixel(57, east)
    pixel(67, east)

# Function to draw a box with a specific color
def box(white):
    buttonid = [73, 74, 75, 66, 56, 46, 35, 34, 33, 42, 52, 62]
    for i in buttonid:
        pixel(i, white)

# Initialize buttons with their default colors
initialize_buttons()  

# Functions to handle button presses and releases, updating colors
def pressnorth(): 
    print("NORTH")
    pixel(64, 3)  # Change color to indicate press
    for i in [83, 84, 85]:
        pixel(i, 3)  

def releasenorth(): 
    pixel(64, ogcolour[64])  # Reset to original color on release
    for i in [83, 84, 85]:
        pixel(i, ogcolour[i]) 

def presssouth(): 
    print("SOUTH")
    pixel(44, 3)  # Change color to indicate press
    for i in [23, 24, 25]:
        pixel(i, 3) 

def releasesouth():  
    pixel(44, ogcolour[44])  # Reset to original color on release
    for i in [23, 24, 25]:
        pixel(i, ogcolour[i]) 

def presswest():  
    print("WEST")
    pixel(53, 3)  # Change color to indicate press
    for i in [51, 61, 41]:
        pixel(i, 3) 

def releasewest(): 
    pixel(53, ogcolour[53])  # Reset to original color on release
    for i in [51, 61, 41]:
        pixel(i, ogcolour[i]) 

def presseast(): 
    print("EAST")
    pixel(55, 3)  # Change color to indicate press
    for i in [57, 67, 47]:
        pixel(i, 3)  

def releaseeast(): 
    pixel(55, ogcolour[55])  # Reset to original color on release
    for i in [57, 67, 47]:
        pixel(i, ogcolour[i]) 

def pressmiddle(): 
    print("PLAYER'S POSITION")

# Event loop to handle button press/release inputs from the Launchpad
for msg in inport:  # Input commands from Launchpad
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 64:
            if msg.velocity != 0:  # North button pressed
                pressnorth() 
            else:  # North button released
                releasenorth()  
        elif msg.note == 44:
            if msg.velocity != 0:  # South button pressed
                presssouth() 
            else:  # South button released
                releasesouth()  
        elif msg.note == 53:
            if msg.velocity != 0:  # West button pressed
                presswest() 
            else:  # West button released
                releasewest() 
        elif msg.note == 55:
            if msg.velocity != 0:  # East button pressed
                presseast()  
            else:  # East button released
                releaseeast()  
        elif msg.note == 54 and msg.velocity != 0:  # Middle button pressed
            pressmiddle()  

