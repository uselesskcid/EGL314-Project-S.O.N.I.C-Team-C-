import mido
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad) # output port for sending commands
inport = mido.open_input(midipad) # input port for feedback from launchpad
def pixel(buttonid, colour): #function to light up 1 pixel
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

def button1(northeast):
    pixel(75, northeast)
button1(63)

def button2(east):
    pixel(65, east)
button2(4)

def button3(southeast):
    pixel(55, southeast)
button3(30)

def button4(southwest):
    pixel(53, southwest)
button4(10)

def button5(west):
    pixel(63, west)
button5(53)

def button6(northwest):
    pixel(73, northwest)
button6(40)




def NW(speaker):
	pixel(81, speaker)
NW(40)

def W(speaker):
	pixel(61, speaker)
W(53)

def SW(speaker):
	pixel(41, speaker)
SW(10)

def NE(speaker):
	pixel(87, speaker)
NE(63)

def E(speaker):
	pixel(67, speaker)
E(4)

def SE(speaker):
	pixel(47, speaker)
SE(30)



def middle(white):
	pixel(64, white)
middle(3)

def box(white):
	buttonid = [82, 83, 84, 85, 86, 76, 66, 56, 46, 45, 44, 43, 42, 52, 62, 72]
	for i in buttonid:
		pixel(i, white)
box(3)
            
def pressNE():
    
    print("North East has been pressed" )
    

def pressE():
    
    print("East has been pressed" )
    
def pressSE():
    
    print("South East has been pressed" )

def pressSW():
    
    print("South West has been pressed" )	

def pressW():
    
    print("West has been pressed" )

def pressNW():
    
    print("North West has been pressed" )
    

    

for msg in inport:
    if msg.type == 'note_on' and msg.note == 75  and msg.velocity != 0:
        pressNE()
    elif msg.type == 'note_on' and msg.note == 65 and msg.velocity != 0:
        pressE()
    elif msg.type == 'note_on' and msg.note == 55 and msg.velocity != 0:
        pressSE()
    elif msg.type == 'note_on' and msg.note == 53 and msg.velocity != 0:
        pressSW()
    elif msg.type == 'note_on' and msg.note == 63 and msg.velocity != 0:
        pressW()
    elif msg.type == 'note_on' and msg.note == 73 and msg.velocity != 0:
        pressNW()
	
