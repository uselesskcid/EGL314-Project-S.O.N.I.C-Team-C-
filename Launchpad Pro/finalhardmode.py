 import mido

# Set up Launchpad MIDI ports for input and output
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # Output port for sending commands to Launchpad
inport = mido.open_input(midipad)  # Input port for receiving feedback from Launchpad

# Dictionary to store original colors for each button
ogcolour = {                             
    81: 37,  # Colours for NORTH WEST
    73: 37,  
    51: 53,  # Colours for WEST
    53: 53,  
    33: 10,  # Colours for SOUTH WEST
    21: 10,  
    35: 45,  # Colours for SOUTH EAST
    27: 45,  
    55: 4,   # Colours for EAST
    57: 4,  
    75: 30,  # Colours for NORTH EAST
    87: 30 
}

# Function to set the color of a specific button
def pixel(buttonid, colour):
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)  # OUTPUT COMMAND TO LAUNCHPAD

# Function to initialize the buttons with their original colors
def initialize_buttons():
    button1(30)
    button2(4)
    button3(45)
    button4(10)
    button5(53)
    button6(37)
    middle(3)
    NW(37)
    W(53)
    SW(10)
    NE(30)
    E(4)
    SE(45)
    box(3)

# Individual button functions to set their colors
def button1(NE):     
    pixel(75, NE)

def button2(E):
    pixel(55, E)

def button3(SE):
    pixel(35, SE)

def button4(SW):
    pixel(33, SW)

def button5(W):
    pixel(53, W)

def button6(NW):
    pixel(73, NW)

# Functions to set colors for additional buttons
def NW(speaker):       
    pixel(81, speaker)

def W(speaker):
    pixel(51, speaker)

def SW(speaker):
    pixel(21, speaker)

def NE(speaker):
    pixel(87, speaker)

def E(speaker):
    pixel(57, speaker)

def SE(speaker):
    pixel(27, speaker)

def middle(white):
    pixel(54, white)

# Function to draw a box with a specific color
def box(white):
    buttonid = [82, 83, 84, 85, 86, 76, 66, 56, 46, 36, 26, 25, 24, 23, 22, 32, 42, 52, 62, 72]
    for i in buttonid:
        pixel(i, white)

# Initialize buttons with their default colors
initialize_buttons()  

# Functions to handle button presses and releases, updating colors
def pressNE():
    print("NORTH EAST")
    pixel(75, 3)  # Change to white
    pixel(87, 3)  # Change to white

def releaseNE(): 
    pixel(75, ogcolour[75])  # Change back to original color
    pixel(87, ogcolour[87])  # Change back to original color

def pressE(): 
    print("EAST")
    pixel(55, 3)  # Change to white
    pixel(57, 3)  # Change to white

def releaseE():
    pixel(55, ogcolour[55])  # Change back to original color
    pixel(57, ogcolour[57])  # Change back to original color

def pressSE(): 
    print("SOUTH EAST")
    pixel(35, 3)  # Change to white
    pixel(27, 3)  # Change to white

def releaseSE(): 
    pixel(35, ogcolour[35])  # Change back to original color
    pixel(27, ogcolour[27])  # Change back to original color

def pressSW(): 
    print("SOUTH WEST")
    pixel(33, 3)  # Change to white
    pixel(21, 3)  # Change to white

def releaseSW(): 
    pixel(33, ogcolour[33])  # Change back to original color
    pixel(21, ogcolour[21])  # Change back to original color

def pressW(): 
    print("WEST")
    pixel(53, 3)  # Change to white
    pixel(51, 3)  # Change to white

def releaseW(): 
    pixel(53, ogcolour[53])  # Change back to original color
    pixel(51, ogcolour[51])  # Change back to original color

def pressNW(): 
    print("NORTH WEST")
    pixel(73, 3)  # Change to white
    pixel(81, 3)  # Change to white

def releaseNW(): 
    pixel(73, ogcolour[73])  # Change back to original color
    pixel(81, ogcolour[81])  # Change back to original color

# Event loop to handle button press/release inputs from the Launchpad
for msg in inport:  # INPUT COMMANDS TO LAUNCHPAD
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 75:
            if msg.velocity != 0:  # When North East pressed
                pressNE()
            else:  # When North East is released
                releaseNE() 
        elif msg.note == 55:
            if msg.velocity != 0:  # When East pressed
                pressE()
            else:  # When East is released
                releaseE() 
        elif msg.note == 35:
            if msg.velocity != 0:  # When South East pressed
                pressSE()
            else:  # When South East is released
                releaseSE()
        elif msg.note == 33:
            if msg.velocity != 0:  # When South West pressed
                pressSW()  
            else:  # When South West is released
                releaseSW()
        elif msg.note == 53:
            if msg.velocity != 0:  # When West pressed
                pressW()
            else:  # When West is released
                releaseW()
        elif msg.note == 73:
            if msg.velocity != 0:  # When North West pressed
                pressNW()
            else:  # When North West is released
                releaseNW()
