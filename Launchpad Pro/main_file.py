import mido
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad) # output port for sending commands
inport = mido.open_input(midipad) # input port for feedback from launchpad

ogcolour = {
    81: 40,  # Colours for NORTH WEST
    73: 40,  
    51: 53,  # Colours foR WEST
    53: 53,  
    33: 10,  # Colours for SOUTH WEST
    21: 10,  
    35: 30,  # Colours for SOUTH EAST
    27: 30,  
    55: 4,  # Colours for EAST
    57: 4,  
    75: 63,  # Colours for NORTH EAST
    87: 63,  
    
}

def pixel(buttonid, colour): #function to light up 1 pixel
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

def initialize_buttons():
    pixel(64, ogcolour[64])
    for i in range(83, 86):
        pixel(i, ogcolour[i])
    button1(63)
    button2(55)
    button3(30)
    button4(10)
    button5(53)
    button6(40)
    middle(3)
    NW(40)
    W(53)
    SW(10)
    NE(63)
    E(4)
    SE(30)
    box(3)

def button1(northeast):
    pixel(75, northeast)

def button2(east):
    pixel(55, east)

def button3(southeast):
    pixel(35, southeast)

def button4(southwest):
    pixel(33, southwest)

def button5(west):
    pixel(53, west)

def button6(northwest):
    pixel(73, northwest)




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

def box(white):
	buttonid = [82, 83, 84, 85, 86, 76, 66, 56, 46, 36, 26, 25, 24, 23, 22, 32, 42, 52, 62, 72]
	for i in buttonid:
		pixel(i, white)
            
def pressNE():
    
    print("NORTH EAST" )
    pixel(75, 3)  # Change to white
    pixel(87, 3)  # Change to white

def releaseNE():
    pixel(75, ogcolour[75])  # Change back to original color
    pixel(87, ogcolour[87])  # Change back to original color

def pressE():
    
    print("EAST" )
    pixel(55, 3)  # Change to white
    pixel(57, 3)  # Change to white

def releaseE():
    pixel(55, ogcolour[55])  # Change back to original color
    pixel(57, ogcolour[57])  # Change back to original color

def pressSE():
    
    print("SOUTH EAST" )
    pixel(35, 3)  # Change to white
    pixel(27, 3)  # Change to white

def releaseSE():
    pixel(35, ogcolour[35])  # Change back to original color
    pixel(27, ogcolour[27])  # Change back to original color

def pressSW():
    
    print("SOUTH WEST" )
    pixel(33, 3)  # Change to white
    pixel(21, 3)  # Change to white

def releaseSW():
    pixel(33, ogcolour[33])  # Change back to original color
    pixel(21, ogcolour[21])  # Change back to original color

def pressW():
    
    print("WEST" )
    pixel(53, 3)  # Change to white
    pixel(51, 3)  # Change to white

def releaseW():
    pixel(73, ogcolour[53])  # Change back to original color
    pixel(81, ogcolour[51])  # Change back to original color

def pressNW():
    
    print("NORTH WEST" )
    pixel(73, 3)  # Change to white
    pixel(81, 3)  # Change to white

def releaseNW():
    pixel(73, ogcolour[73])  # Change back to original color
    pixel(81, ogcolour[81])  # Change back to original color



    
# Press for feedback function
for msg in inport:
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 75:
            if msg.velocity != 0:  # When North East pressed
                pressNE()
            else:   # When North East is released
                releaseNE()
        elif msg.note == 55:
            if msg.velocity != 0:  
                pressE()
            else: 
                releaseE()  
        elif msg.note == 35:
            if msg.velocity != 0:  
                pressSE()
            else: 
                releaseSE() 
        elif msg.note == 33:
            if msg.velocity != 0:  
                pressSW()
            else: 
                releaseSW() 
        elif msg.note == 53:
            if msg.velocity != 0:  
                pressW()
            else: 
                releaseW()    
        elif msg.note == 73:
            if msg.velocity != 0: 
                pressNW()
            else: 
                releaseNW()  
                                                                                                                          