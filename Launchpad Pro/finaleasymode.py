import mido

midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # output port for sending commands
inport = mido.open_input(midipad)  # input port for feedback from launchpad

# Dictionary to store original colors 
#ouput command for sending colour\/
ogcolour = {     
    64: 10,  # Colours for NORTH
    83: 10,  
    84: 10, 
    85: 10,
    44: 4,   # Colours for South
    23: 4,
    24: 4,
    25: 4,   
    55: 40,  # Colours for EAST
    57: 40,
    47: 40,
    67: 40,
    53: 30,    # Colours for WEST
    51: 30,
    41: 30,
    61: 30
    
    
    
    
    
    
    
}

# Function to light up 1 pixel
#output command for setting up colour \/
def pixel(buttonid, colour): 
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

# Initialize button colors
#output command for setting up colour \/
def initialize_buttons(): 
    pixel(64, ogcolour[64])
    for i in range(83, 86):
        pixel(i, ogcolour[i])
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
#output command for setting up colour \/
def buttonnorth(nbutton):
    pixel(64, nbutton)
#output command for setting up colour \/
def buttonsouth(sbutton):
    pixel(44, sbutton)
#output command for setting up colour \/
def buttonwest(wbutton):
    pixel(53, wbutton)
#output command for setting up colour \/
def buttoneast(ebutton):
    pixel(55, ebutton)
#output command for setting up colour \/
def middlebutton(mbutton):
    pixel(54, mbutton)
#output command for setting up colour \/
def nfill(north):
    for i in range(83, 86):
        pixel(i, north)
#output command for setting up colour \/
def sfill(south):    #output command for setting up colour \/
    for i in range(23, 26):
        pixel(i, south)
#output command for setting up colour \/
def wfill(west):
    pixel(41, west)
    pixel(51, west)
    pixel(61, west)
#output command for setting up colour \/
def etfill(east):
    pixel(47, east)
    pixel(57, east)
    pixel(67, east)
#output command for setting up colour \/
def box(white):
    buttonid = [73, 74, 75, 66, 56, 46, 35, 34, 33, 42, 52, 62]
    for i in buttonid:
        pixel(i, white)
#output command for setting up colour \/
initialize_buttons()


# Direction functions
 #input feedback from buttons  \/
def pressnorth(): 
    print("NORTH")
    pixel(64, 3)  # Change to white
    for i in [83, 84, 85]:
        pixel(i, 3)  # Change to white
 #input feedback from buttons  \/
def releasenorth(): 
    pixel(64, ogcolour[64])  # Change back to original color
    for i in [83, 84, 85]:
        pixel(i, ogcolour[i])  # Change back to original color
 #input feedback from buttons  \/
def presssouth():    #input feedback from buttons  \/
    print("SOUTH")
    pixel(44, 3)  # Change to white
    for i in [23, 24, 25]:
        pixel(i, 3)  # Change to white
 #input feedback from buttons  \/
def releasesouth():    #input feedback from buttons   \/
    pixel(44, ogcolour[44])  # Change back to original color
    for i in [23, 24, 25]:
        pixel(i, ogcolour[i])  # Change back to original color
 #input feedback from buttons  \/
def presswest():    #input feedback from buttons     \/
    print("WEST")
    pixel(53, 3)  # Change to white
    for i in [51, 61, 41]:
        pixel(i, 3)  # Change to white
 #input feedback from buttons  \/
def releasewest():         #input feedback from buttons    \/
    pixel(53, ogcolour[53])  # Change back to original color
    for i in [51, 61, 41]:
        pixel(i, ogcolour[i])  # Change back to original color
 #input feedback from buttons  \/
def presseast():     #input feedback from buttons     \/
    print("EAST")
    pixel(55, 3)  # Change to white
    for i in [57, 67, 47]:
        pixel(i, 3)  # Change to white
 #input feedback from buttons  \/
def releaseeast():  #input feedback from buttons     \/
    pixel(55, ogcolour[55])  # Change back to original color
    for i in [57, 67, 47]:
        pixel(i, ogcolour[i])  # Change back to original color



 #input feedback from buttons  \/
def pressmiddle():   
    print("PLAYER'S POSITION")

# Press for feedback function 
 #input feedback from buttons  \/
for msg in inport:    
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 64:
            if msg.velocity != 0:  # North pressed
                pressnorth()
            else:  # North released
                releasenorth()
        elif msg.note == 44:
            if msg.velocity != 0:  # South pressed
                presssouth()
            else: 
                releasesouth() # South released
            
        elif msg.note == 53:
            if msg.velocity != 0:  # West pressed
                presswest()
            else: 
                releasewest() # West released
        elif msg.note == 55: 
            if msg.velocity != 0:  # East pressed
                presseast()
            else: 
                releaseeast() # East released
        elif msg.note == 54 and msg.velocity != 0:
            pressmiddle()


