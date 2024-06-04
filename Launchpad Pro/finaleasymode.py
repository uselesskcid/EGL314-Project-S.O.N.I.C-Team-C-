
	
import mido
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad) # output port for sending commands
inport = mido.open_input(midipad) # input port for feedback from launchpad

#output command for setting colour \/
ogcolour = {                             
    81: 37,  # Colours for NORTH WEST
    73: 37,  
    51: 53,  # Colours foR WEST
    53: 53,  
    33: 10,  # Colours for SOUTH WEST
    21: 10,  
    35: 45,  # Colours for SOUTH EAST
    27: 45,  
    55: 4,  # Colours for EAST
    57: 4,  
    75: 30,  # Colours for NORTH EAST
    87: 30 
    
}

#output command for setting colour \/
def pixel(buttonid, colour): #function to light up 1 pixel (output command to set up colour) \/
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

#output command for setting colour \/
def initialize_buttons(): #output command to set up colour \/
    
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

#output command for setting colour \/
def button1(NE):     #output command to set up colour \/
    pixel(75, NE)

#output command for setting colour \/
def button2(E):
    pixel(55, E)

#output command for setting colour \/
def button3(SE):
    pixel(35, SE)

#output command for setting colour \/
def button4(SW):
    pixel(33, SW)

#output command for setting colour \/
def button5(W):
    pixel(53, W)

#output command for setting colour \/
def button6(NW):
    pixel(73, NW)



#output command for setting colour \/
def NW(speaker):       
    pixel(81, speaker)

#output command for setting colour \/
def W(speaker):
    pixel(51, speaker)

#output command for setting colour \/
def SW(speaker):
    pixel(21, speaker)

#output command for setting colour \/
def NE(speaker):
    pixel(87, speaker)

#output command for setting colour \/
def E(speaker):
    pixel(57, speaker)

#output command for setting colour \/
def SE(speaker):
    pixel(27, speaker)


#output command for setting colour \/
def middle(white):
    pixel(54, white)


#output command for setting colour \/
def box(white):
    buttonid = [82, 83, 84, 85, 86, 76, 66, 56, 46, 36, 26, 25, 24, 23, 22, 32, 42, 52, 62, 72]
    for i in buttonid:
        pixel(i, white)

initialize_buttons() #output command
            
def pressNE(): #input feedback \/
    
    print("NORTH EAST" )
    pixel(75, 3)  # Change to white
    pixel(87, 3)  # Change to white
 
def releaseNE(): #input feedback \/
    pixel(75, ogcolour[75])  # Change back to original color
    pixel(87, ogcolour[87])  # Change back to original color

def pressE(): #input feedback \/
    
    print("EAST" )
    pixel(55, 3)  # Change to white
    pixel(57, 3)  # Change to white

def releaseE(): #input feedback \/
    pixel(55, ogcolour[55])  # Change back to original color
    pixel(57, ogcolour[57])  # Change back to original color

def pressSE(): #input feedback \/
    
    print("SOUTH EAST" )
    pixel(35, 3)  # Change to white
    pixel(27, 3)  # Change to white

def releaseSE(): #ouput command for sending colour
    pixel(35, ogcolour[35])  # Change back to original color
    pixel(27, ogcolour[27])  # Change back to original color

def pressSW(): #input feedback \/
    
    print("SOUTH WEST" )
    pixel(33, 3)  # Change to white
    pixel(21, 3)  # Change to white

def releaseSW(): #ouput command for sending colour
    pixel(33, ogcolour[33])  # Change back to original color
    pixel(21, ogcolour[21])  # Change back to original color

def pressW(): #input feedback \/
    
    print("WEST" )
    pixel(53, 3)  # Change to white
    pixel(51, 3)  # Change to white

def releaseW(): #ouput command for sending colour
    pixel(53, ogcolour[53])  # Change back to original color
    pixel(51, ogcolour[51])  # Change back to original color

def pressNW(): #input feedback \/
    
    print("NORTH WEST" )
    pixel(73, 3)  # Change to white
    pixel(81, 3)  # Change to white

def releaseNW(): #ouput command for sending colour
    pixel(73, ogcolour[73])  # Change back to original color
    pixel(81, ogcolour[81])  # Change back to original color



    
# Press for feedback function
for msg in inport:                                          #input feedback \/
    if msg.type == 'note_on' or msg.type == 'note_off': 
        if msg.note == 75:
            if msg.velocity != 0:  # When North East pressed
		#input feedback
                pressNE()
            else:   # When North East is released
		
                releaseNE() #output command
		
        elif msg.note == 55:
            if msg.velocity != 0:   #input feedback
                pressE()
            else: 
                releaseE()  #output command
		
        elif msg.note == 35:
            if msg.velocity != 0:  #input feedback
                pressSE()
            else: 
                releaseSE() #output command
		
        elif msg.note == 33:
            if msg.velocity != 0:  #input feedback
                pressSW()  
            else: 
                releaseSW() #output command
		
        elif msg.note == 53:
            if msg.velocity != 0:  #input feedback
                pressW()
            else: 
                releaseW()  #output command
		  
        elif msg.note == 73:
            if msg.velocity != 0: 
                pressNW()
            else: 
                releaseNW()  #output command
