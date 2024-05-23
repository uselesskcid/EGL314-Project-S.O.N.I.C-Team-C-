import mido
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad) # output port for sending commands
inport = mido.open_input(midipad) # input port for feedback from launchpad
def pixel(buttonid, colour): #function to light up 1 pixel
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

def button1(top):
    pixel(64, top)
button1(10)

def button2(middle):
    pixel(54, middle)
button2(4)

def button3(bottom):
    pixel(44, bottom)
button3(30)





def group1(speakers1):
	buttonid = [71, 77]
	for i in buttonid:
		pixel(i, speakers1)
group1(10)

def group2(speakers2):
	buttonid = [51, 57]
	for i in buttonid:
		pixel(i, speakers2)
group2(4)

def group3(speakers3):
	buttonid = [31, 37]
	for i in buttonid:
		pixel(i, speakers3)
group3(30)

def presstop():
    
    print("top has been pressed" )
    

def pressmiddle():
    
    print("middle has been pressed" )
    
def pressbottom():
    
    print("bottom has been pressed" )
    

    

for msg in inport:
    if msg.type == 'note_on' and msg.note == 64  and msg.velocity != 0:
        presstop()
    elif msg.type == 'note_on' and msg.note == 54 and msg.velocity != 0:
        pressmiddle()
    elif msg.type == 'note_on' and msg.note == 44 and msg.velocity != 0:
        pressbottom()