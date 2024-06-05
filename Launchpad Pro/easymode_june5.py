import mido

# Set up Launchpad MIDI ports for input and output
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # Output port for sending commands to Launchpad
inport = mido.open_input(midipad)  # Input port for receiving feedback from Launchpad

# Dictionary to store original colors for each button
ogcolour = {
    
    55: 40,  # Colors for RIGHT
    57: 40,
    47: 40,
    67: 40,
    76: 40,
    36: 40,
    53: 30,  # Colors for LEFT
    51: 30,
    41: 30,
    61: 30,
    72: 30,
    32: 30
}

# Function to set the color of a specific button
def pixel(buttonid, colour):
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)  # Output command to Launchpad

# Function to initialize the buttons with their original colors
def initialize_buttons():
  
    # Set initial colors for other buttons and rows/columns
    buttonleft(30)
    buttonright(40)
    middlebutton(3)
    lfill(30)
    rfill(40)
    box(3)

# Individual button functions to set their colors


def buttonleft(lbutton):
    pixel(53, lbutton)

def buttonright(rbutton):
    pixel(55, rbutton)

def middlebutton(mbutton):
    pixel(54, mbutton)

# Functions to fill rows or columns with a specific color

def lfill(west):
    pixel(41, west)
    pixel(51, west)
    pixel(61, west)
    pixel(72, west)
    pixel(32, west)

def rfill(east):
    pixel(47, east)
    pixel(57, east)
    pixel(67, east)
    pixel(76, east)
    pixel(36, east)

# Function to draw a box with a specific color
def box(white):
    buttonid = [66, 56, 46, 42, 52, 62]
    for i in buttonid:
        pixel(i, white)

# Initialize buttons with their default colors
initialize_buttons()  

# Functions to handle button presses and releases, updating colors

def pressleft():  
    print("LEFT")
    pixel(53, 3)  # Change color to indicate press
    for i in [51, 61, 41, 72, 32]:
        pixel(i, 3) 

def releaseleft(): 
    pixel(53, ogcolour[53])  # Reset to original color on release
    for i in [51, 61, 41, 72, 32]:
        pixel(i, ogcolour[i]) 

def pressright(): 
    print("RIGHT")
    pixel(55, 3)  # Change color to indicate press
    for i in [57, 67, 47, 76, 36]:
        pixel(i, 3)  

def releaseright(): 
    pixel(55, ogcolour[55])  # Reset to original color on release
    for i in [57, 67, 47, 76, 36]:
        pixel(i, ogcolour[i]) 

def pressmiddle(): 
    print("PLAYER'S POSITION")

# Event loop to handle button press/release inputs from the Launchpad
for msg in inport:  # Input commands from Launchpad
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 53:
            if msg.velocity != 0:  # Left button pressed
                pressleft() 
            else:  # Left button released
                releaseleft()  
        elif msg.note == 55:
            if msg.velocity != 0:  #Right button pressed
                pressright()  
            else:  # Right button released
                releaseright()  
        elif msg.note == 54 and msg.velocity != 0:  # Middle button pressed
            pressmiddle()  