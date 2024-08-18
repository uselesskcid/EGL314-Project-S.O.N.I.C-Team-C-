from pythonosc import osc_server, dispatcher
from pythonosc import udp_client
import time
from threading import Thread

TeamA_Pi = "192.168.254.49"
TeamA_Port = 2000
Addr = "/print"

NeoPixel_Pi = "192.168.254.242"
NeoPixel_Port = 2005

Balloon_Pi = "192.168.254.102"
Balloon_Port = 2006

# ============================ OSC CLients ====================== #
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)
		#print("Message sent successfully.")

	except:
		print("Message not sent")

# Create OSC clients
truss_client = udp_client.SimpleUDPClient(NeoPixel_Pi, NeoPixel_Port)
balloon_client = udp_client.SimpleUDPClient(Balloon_Pi, Balloon_Port)


# ================================ NEOPIXEL TRUSS DEFINITION SECTION =================================== #

def send_color_array_truss(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    truss_client.send_message(address, flattened_colors)
    #print(f"Sent color array to Truss: {flattened_colors}")

def send_brightness_truss(brightness):
    truss_client.send_message("/brightness", brightness)
    #print(f"Sent brightness to Truss: {brightness}")

def send_off_truss():
    truss_client.send_message("/off", [])
    print("Sent off message to Truss")

def blink_color(NUM_PIXELS, color, blink_duration):
    blink_end_time = time.time() + blink_duration
    while time.time() < blink_end_time:
        # Blink color
        colors = [color] * NUM_PIXELS
        send_color_array_truss(colors)
        time.sleep(0.1)  # Short on time
        # Turn off
        colors = [(0, 0, 0)] * NUM_PIXELS
        send_color_array_truss(colors)
        time.sleep(0.1)  # Short off time

def gradual_on(NUM_PIXELS, duration):
    step_delay = duration / NUM_PIXELS
    for i in range(NUM_PIXELS + 1):  # Include the final state where all pixels are on
        colors = [(255, 255, 255) if j < i else (0, 0, 0) for j in range(NUM_PIXELS)]
        send_color_array_truss(colors)
        time.sleep(step_delay)
    # Turn off the Truss LEDs right after the gradual on effect completes
    send_off_truss()

def blink_sequence(NUM_PIXELS, duration):
    end_time = time.time() + duration
    colors_sequence = [
        (255, 0, 0),  # Red
        (0, 0, 255),  # Blue
        (0, 255, 0),  # Green
    ]
    
    while time.time() < end_time:
        for color in colors_sequence:
            blink_color(NUM_PIXELS, color, 0.5)  # Blink each color for 0.5 seconds

def red_blink_sequence(NUM_PIXELS, duration):
    red_end_time = time.time() + duration
    colors_sequence = [
        (255, 0, 0),  # Red
        (255, 255, 255) # white
    ]
    
    while time.time() < red_end_time:
        for color in colors_sequence:
            blink_color(NUM_PIXELS, color, 1.2)  # Blink each color for 2 seconds

def green_blink_sequence(NUM_PIXELS, duration):
    green_end_time = time.time() + duration
    colors_sequence = [
        (0, 255, 0),  # Green
        (255, 255, 255) # white
    ]
    
    while time.time() < green_end_time:
        for color in colors_sequence:
            blink_color(NUM_PIXELS, color, 1.8)  # Blink each color for 2 seconds

def blue_blink_sequence(NUM_PIXELS, duration):
    blue_end_time = time.time() + duration
    colors_sequence = [
        (0, 0, 255),  # Blue
        (255, 255, 255) # white
    ]
    
    while time.time() < blue_end_time:
        for color in colors_sequence:
            blink_color(NUM_PIXELS, color, 1.3)  # Blink each color for 2 seconds

def purple_blink_sequence(NUM_PIXELS, duration):
    blue_end_time = time.time() + duration
    colors_sequence = [
        (255, 0, 255),  # probably not purple
        (255, 255, 255) # white
    ]
    
    while time.time() < blue_end_time:
        for color in colors_sequence:
            blink_color(NUM_PIXELS, color, 1.6)  # Blink each color for 2 seconds

def change_colour_sequence(NUM_PIXELS):
    colors = [(0, 0, 0)] * NUM_PIXELS
    send_color_array_truss(colors)

# ================================ NEOPIXEL BALLOON DEFINITION SECTION =================================== #

def send_color_array_balloon(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    balloon_client.send_message(address, flattened_colors)
    print(f"Sent color array to Balloon: {flattened_colors}")

def send_brightness_balloon(brightness):
    balloon_client.send_message("/brightness", brightness)
    print(f"Sent brightness to Balloon: {brightness}")

def send_off_balloon():
    balloon_client.send_message("/off", [])
    print("Sent off message to Balloon")

def meteor_effect(NUM_PIXELS, duration, speed, meteor_size):
    end_time = time.time() + duration
    position = 0
    
    while time.time() < end_time:
        # Create meteor effect
        colors = [(0, 0, 0)] * NUM_PIXELS
        for i in range(position, position + meteor_size):
            if i < NUM_PIXELS:
                colors[i] = (0, 0, 0)  # Purple color
        
        send_color_array_balloon(colors)
        time.sleep(speed)
        
        # Clear the effect
        colors = [(0, 0, 0)] * NUM_PIXELS
        send_color_array_balloon(colors)
        time.sleep(speed)
        
        # Move meteor position
        position += 1
        if position >= NUM_PIXELS:
            position = 0  # Loop the meteor effect

# ===================================== LASER DEFINITION SECTION ======================================= #
def EveryLaserOn():
    seq = ["2,1,1", "2,2,1", "5,1,1", "5,2,1", "8,1,1", "8,2,1", "11,1,1", "11,2,1"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def EveryLaserOff():
    seq = ["2,1,0", "2,2,0", "5,1,0", "5,2,0", "8,1,0", "8,2,0", "11,1,0", "11,2,0"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerSide1():
    seq = ["2,1,1", "2,2,1", "5,1,0", "5,2,0", "8,1,1", "8,2,1", "11,1,0", "11,2,0"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerSide2():
    seq = ["2,1,0", "2,2,0", "5,1,1", "5,2,1", "8,1,0", "8,2,0", "11,1,1", "11,2,1"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerCorner1():
    seq = ["2,1,1", "2,2,1", "5,1,1", "5,2,1", "8,1,0", "8,2,0", "11,1,0", "11,2,0"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerCorner2():
    seq = ["2,1,0", "2,2,0", "5,1,0", "5,2,0", "8,1,1", "8,2,1", "11,1,1", "11,2,1"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerTeamC():
    seq = ["2,1,1", "2,2,1", "5,1,0", "5,2,0", "8,1,0", "8,2,0", "11,1,0", "11,2,0"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerTeamE():
    seq = ["2,1,0", "2,2,0", "5,1,1", "5,2,1", "8,1,0", "8,2,0", "11,1,0", "11,2,0"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerTeamB():
    seq = ["2,1,0", "2,2,0", "5,1,0", "5,2,0", "8,1,1", "8,2,1", "11,1,0", "11,2,0"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

def SpeakerTeamF():
    seq = ["2,1,0", "2,2,0", "5,1,0", "5,2,0", "8,1,0", "8,2,0", "11,1,1", "11,2,1"]
    for x in seq:
        send_message(TeamA_Pi, TeamA_Port, Addr, x)

# ===================================== TEAM LASER SECTION ======================================= #
# Speaker Number, Laser Module, On/Off
# === On === #
	
def teamLaserThree_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 1"])
    print('Laser 3 on')

def teamLaserFour_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 1"])
    print('Laser 4 on')

def teamAllLasers_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 1"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 1"])
	
# === Off === #

  
def teamLaserThree_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 0"])
  print('Laser 3 off')
def teamLaserFour_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 0"])
  print('Laser 4 off')

def teamAllLasers_Off():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 0"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 0"])

# ===================================== LASER SEQUENCE SECTION ======================================= #

def LaserSequence():
    NUM_PIXELS_TRUSS = 170  # Adjusted to 170 pixels for Truss
    NUM_PIXELS_BALLOON = 101  # Adjusted to 101 pixels for Balloon
    duration = 27  # Duration of Riser Effect.
    meteor_size = 15  # Size of the meteor effect
    meteor_speed = 0.03  # Speed of the meteor effect (faster) 
    meteor_duration = 7.5  # Duration for meteor effect and final blinking sequence

    BeatsPerMinute = 60/71.6 # Time interval between beats
    Counter = 0
    start_time = time.time()
    EveryLaserOff()
    while time.time() - start_time < 61 :
        time.sleep(BeatsPerMinute)
        EveryLaserOff()
        if (Counter == 1):
            EveryLaserOn()
        if (Counter == 2):
            EveryLaserOff()
        if (Counter == 3):
            EveryLaserOn()
        if (Counter == 4):
            EveryLaserOff()
        if (Counter == 5):
            EveryLaserOn()
        if (Counter == 6):
            EveryLaserOff()
        if (Counter == 7):
            SpeakerSide1()
        if (Counter == 8):
            SpeakerSide2()
        if (Counter == 9):
            SpeakerSide1()
        if (Counter == 10):
            SpeakerSide2()
        if (Counter == 11):
            SpeakerSide1()      
        if (Counter == 12):
            SpeakerSide2()
        if (Counter == 13):
            SpeakerCorner1()
        if (Counter == 14):
            SpeakerCorner2()
        if (Counter == 15):
            SpeakerCorner1()
        if (Counter == 16):
            SpeakerCorner2()
        if (Counter == 17):
            SpeakerCorner1()
        if (Counter == 18):
            SpeakerCorner2()
        if (Counter == 19):
            SpeakerCorner1()
        if (Counter == 20):
            SpeakerCorner2()
        if (Counter == 21):
            SpeakerTeamC()
        if (Counter == 22):
            SpeakerTeamE()
        if (Counter == 23):
            SpeakerTeamB()
        if (Counter == 24):
            SpeakerTeamF()
        if (Counter == 25):
            SpeakerTeamC()
        if (Counter == 26):
            SpeakerTeamE()
        if (Counter == 27):
            SpeakerTeamB()
        if (Counter == 28):
            SpeakerTeamF()
        if (Counter == 29):
            EveryLaserOff()
        if (Counter == 30):
            EveryLaserOn()
        if (Counter == 31):
            EveryLaserOff()
        if (Counter == 32):
            EveryLaserOn()
        if (Counter == 33):
            EveryLaserOff()
        if (Counter == 34):
            EveryLaserOn()
        if (Counter == 35):
            EveryLaserOff()
        print(Counter)
        Counter += 1

    EveryLaserOff()
        
# ===================================== GUI SECTION ======================================= #