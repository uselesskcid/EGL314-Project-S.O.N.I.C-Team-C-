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