import mido
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad) # output port for sending commands
inport = mido.open_input(midipad) # input port for feedback from launchpad
def pixel(buttonid, colour): #function to light up 1 pixel
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)
#button leds
def buttonnorth(nbutton):
    pixel(64, nbutton)
buttonnorth(10)

def buttonsouth(sbutton):
    pixel(44, sbutton)
buttonsouth(4)

def buttonwest(wbutton):
    pixel(53, wbutton)
buttonwest(30)

def buttoneast(ebutton):
    pixel(55, ebutton)
buttoneast(40)

def middlebutton(mbutton):
    pixel(54, mbutton)
middlebutton(3)





#direction colours
def nfill(north):
    for i in range(83, 86):
        pixel(i, north)
nfill(10)

def sfill(south):
    for i in range(23, 26):
        pixel(i, south)
sfill(4)




def wfill(west):
    pixel(41, west)
    pixel(51, west)
    pixel(61, west)
wfill(30)
def etfill(east):
    pixel(47, east)
    pixel(57, east)
    pixel(67, east)
etfill(40)

#border colour
def box(white):
	buttonid = [72, 73, 74, 75, 76, 66, 56, 46, 36, 35, 34, 33, 32, 42, 52, 62]
	for i in buttonid:
		pixel(i, white)
box(3)
#direction functions
def pressnorth():
    
    print("north has been pressed" )
    

def presssouth():
    
    print("south has been pressed" )
   

def presswest():
    print("west has been pressed" )
   

def presseast():
    print("east has been pressed" )

def pressmiddle():
    print("start game" )
    



#press for feedback function
for msg in inport:
    if msg.type == 'note_on' and msg.note == 64  and msg.velocity != 0:
        pressnorth()
    elif msg.type == 'note_on' and msg.note == 44 and msg.velocity != 0:
        presssouth()
    elif msg.type == 'note_on' and msg.note == 53 and msg.velocity != 0:
        presswest()
    elif msg.type == 'note_on' and msg.note == 55 and msg.velocity != 0:
        presseast()
    elif msg.type == 'note_on' and msg.note == 54 and msg.velocity != 0:
        pressmiddle()


