import mido
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad) # output port for sending commands
inport = mido.open_input(midipad) # input port for feedback from launchpad
def pixel(buttonid, colour): #function to light up 1 pixel
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

def button1(northeast):
    pixel(65, northeast)
button1(10)

def button2(east):
    pixel(55, east)
button2(4)

def button3(southeast):
    pixel(45, southeast)
button3(30)

def button4(southwest):
    pixel(43, southwest)
button4(30)

def button5(west):
    pixel(53, west)
button5(4)

def button6(northwest):
    pixel(63, northwest)
button6(10)





def group1(speakers1):
	buttonid = [71, 78]
	for i in buttonid:
		pixel(i, speakers1)
group1(10)

def group2(speakers2):
	buttonid = [51, 58]
	for i in buttonid:
		pixel(i, speakers2)
group2(4)

def group3(speakers3):
	buttonid = [31, 38]
	for i in buttonid:
		pixel(i, speakers3)
group3(30)

def box(white):
	buttonid = [72, 73, 74, 75, 76, 66, 56, 46, 36, 35, 34, 33, 32, 42, 52, 62]
	for i in buttonid:
		pixel(i, white)
box(3)

def arrow(white):	
	buttonid = [13,14,15,24]
	for i in buttonid:
		pixel(i, white)
arrow(3)

def middle(white):
	pixel(54)
middle(3)
            
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
    if msg.type == 'note_on' and msg.note == 65  and msg.velocity != 0:
        pressNE()
    elif msg.type == 'note_on' and msg.note == 55 and msg.velocity != 0:
        pressE()
    elif msg.type == 'note_on' and msg.note == 45 and msg.velocity != 0:
        pressSE()
    elif msg.type == 'note_on' and msg.note == 43 and msg.velocity != 0:
        pressSW()
    elif msg.type == 'note_on' and msg.note == 53 and msg.velocity != 0:
        pressW()
    elif msg.type == 'note_on' and msg.note == 63 and msg.velocity != 0:
        pressNW()
	