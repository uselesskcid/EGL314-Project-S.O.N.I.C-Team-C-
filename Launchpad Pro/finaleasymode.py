import mido

midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)  # output port for sending commands
inport = mido.open_input(midipad)  # input port for feedback from launchpad

# Dictionary to store original colors
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
def pixel(buttonid, colour): #output command for setting up colour \/
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

# Initialize button colors
def initialize_buttons(): #output command for setting up colour \/
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

def buttonnorth(nbutton): #output command for setting up colour \/
    pixel(64, nbutton)

def buttonsouth(sbutton):
    pixel(44, sbutton)

def buttonwest(wbutton):
    pixel(53, wbutton)

def buttoneast(ebutton):
    pixel(55, ebutton)

def middlebutton(mbutton):
    pixel(54, mbutton)

def nfill(north):
    for i in range(83, 86):
        pixel(i, north)

def sfill(south):    #output command for setting up colour \/
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

def box(white):
    buttonid = [73, 74, 75, 66, 56, 46, 35, 34, 33, 42, 52, 62]
    for i in buttonid:
        pixel(i, white)

initialize_buttons() #output command for setting up colour

# Direction functions
def pressnorth():  #input feedback from buttons  \/
    print("NORTH")
    pixel(64, 3)  # Change to white
    for i in [83, 84, 85]:
        pixel(i, 3)  # Change to white

def releasenorth(): #output command to return original colour \/
    pixel(64, ogcolour[64])  # Change back to original color
    for i in [83, 84, 85]:
        pixel(i, ogcolour[i])  # Change back to original color

def presssouth():    #input feedback from buttons  \/
    print("SOUTH")
    pixel(44, 3)  # Change to white
    for i in [23, 24, 25]:
        pixel(i, 3)  # Change to white

def releasesouth():  #output command to return original colour \/
    pixel(44, ogcolour[44])  # Change back to original color
    for i in [23, 24, 25]:
        pixel(i, ogcolour[i])  # Change back to original color

def presswest():    #input feedback from buttons     \/
    print("WEST")
    pixel(53, 3)  # Change to white
    for i in [51, 61, 41]:
        pixel(i, 3)  # Change to white

def releasewest():        #output command to return original colour \/
    pixel(53, ogcolour[53])  # Change back to original color
    for i in [51, 61, 41]:
        pixel(i, ogcolour[i])  # Change back to original color

def presseast():     #input feedback from buttons     \/
    print("EAST")
    pixel(55, 3)  # Change to white
    for i in [57, 67, 47]:
        pixel(i, 3)  # Change to white

def releaseeast(): #output command to return original colour \/
    pixel(55, ogcolour[55])  # Change back to original color
    for i in [57, 67, 47]:
        pixel(i, ogcolour[i])  # Change back to original color




def pressmiddle():    #input feedback from buttons 
    print("PLAYER'S POSITION")

# Press for feedback function 
for msg in inport:    #input feedback from buttons \/
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 64:
            if msg.velocity != 0:  # North pressed
                pressnorth() #input feedback from buttons 
            else:  # North released
                releasenorth() #output command 
        elif msg.note == 44:
            if msg.velocity != 0:  # South pressed
                presssouth() #input feedback from buttons 
            else: 
                releasesouth() # South released
                               #output command 
            
        elif msg.note == 53:
            if msg.velocity != 0:  # West pressed
                presswest() #input feedback from buttons 
            else: 
                releasewest() # West released
                                #output command 
        elif msg.note == 55: 
            if msg.velocity != 0:  # East pressed
                presseast() #input feedback from buttons 
            else: 
                releaseeast() # East released
                            #output command 
        elif msg.note == 54 and msg.velocity != 0:
            pressmiddle()


