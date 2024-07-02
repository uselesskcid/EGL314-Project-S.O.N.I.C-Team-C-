import mido
import time


# Set up Launchpad MIDI ports for input and output
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'
outport = mido.open_output(midipad)
inport = mido.open_input(midipad)

ogcolour = {
    55: 40,  # Colors for RIGHT
    54: 3,   # Color for middle
    53: 30,   # Colors for LEFT
    11: 3
}


input_block = False


def pixel(buttonid, colour):
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

def initialize_buttons():
    buttonleft(30)
    buttonright(40)
    middlebutton(3)
    startseqbutton(3)

def buttonleft(lbutton):
    pixel(53, lbutton)

def buttonright(rbutton):
    pixel(55, rbutton)

def middlebutton(mbutton):
    pixel(54, mbutton)
    
def startseqbutton(ss):
    pixel(11, ss)
    

def circularpath():
    buttonid = [83, 84, 85, 76, 67, 57, 47, 36, 25, 24, 23, 23, 32, 41, 51, 61, 72]
    startpixel = 0
    startsecondpixel = 1
    startthirdpixel = 2

    while True:
        pixel(buttonid[startpixel - 1], 0)
        pixel(buttonid[startsecondpixel - 1], 0)
        pixel(buttonid[startthirdpixel - 1], 0)
        
        pixel(buttonid[startpixel], 3) 
        pixel(buttonid[startsecondpixel], 3) 
        pixel(buttonid[startthirdpixel], 3)
        time.sleep(0.15)

        startpixel = (startpixel + 1) % len(buttonid)
        startsecondpixel = (startsecondpixel + 1) % len(buttonid)
        startthirdpixel = (startthirdpixel + 1) % len(buttonid)

initialize_buttons()

import threading
threading.Thread(target=circularpath, daemon=True).start()

def pressleft():
    global input_block
    if not input_block:
        print("LEFT")
        pixel(53, 3) 

def releaseleft():
    global input_block
    if not input_block:
        pixel(53, ogcolour[53]) 

def pressright():
    global input_block
    if not input_block:
        print("RIGHT")
        pixel(55, 3) 

def releaseright():
    global input_block
    if not input_block:
        pixel(55, ogcolour[55]) 


        


    
def block_inputs():
    global input_block
    input_block = True
    blockedbuttons = [53, 54, 55]
    
    for button in blockedbuttons:
        pixel(54, 0)
        pixel(11, 0)
        
    time.sleep(30)
    
    for button in blockedbuttons:
        pixel(53, ogcolour[53])
        pixel(54, ogcolour[54])
        pixel(55, ogcolour[55])
        pixel(11, ogcolour[11])
        
    input_block = False


for msg in inport:
    if msg.type == 'note_on' or msg.type == 'note_off':
        if msg.note == 53:
            if msg.velocity != 0:
                pressleft()
            else:
                releaseleft()
        elif msg.note == 55:
            if msg.velocity != 0:
                pressright()
            else:
                releaseright()
       
        elif msg.note == 11:
            if not input_block:
                threading.Thread(target=block_inputs).start()
                    

            

                

        
