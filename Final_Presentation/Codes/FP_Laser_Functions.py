# THIS FILE IS INTENDED TO HAVE FUNCTIONS THAT PLAY REAPER AND MA3, AS WELL AS LASERS AND NEOPIXEL FUNCTIONS THAT ARE SOMEWHERE ELSE.

from pythonosc import udp_client
import time
import FP_Laser_Neopixel as n
import FP_Laser_Sequence as l

def send_message(receiver_ip, receiver_port, address, message):
  try:
    # Create an OSC client to send messages
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

    # Send an OSC message to the receiver
    client.send_message(address, message)

    print("Message sent successfully.")
  except:
    print("Message not sent")
    
# GRANDMA3 SETTINGS RIGHT HERE
MA3_IP = "192.168.254.229"		# MA3 laptop IP
MA3_PORT = 8888 # GRANDMA3 Local listen port
MA3_ADDR = "/gma3/cmd" # Trigger TRUE Value
# msg = "Go Sequence wtv"

# REAPER SETTINGS RIGHT HERE
REA_IP = "192.168.254.30"    # REAPER laptop IP
REA_PORT = 6800 # REAPER Local listen port
REA_MSG = float(1) # Trigger TRUE Value
# addr = "/action & /marker"

def REA_JumpLaserMarker(): #Marker 62, automatically plays
  send_message(REA_IP, REA_PORT, "/marker/62", REA_MSG)
  send_message(REA_IP, REA_PORT, "/action/1007", REA_MSG)
  print('Laser Marker 62 jumped')  
  
def REA_Stop(): #Stop Button
  send_message(REA_IP, REA_PORT, "/action/1016", REA_MSG)
  print('Stop')

def MA3_Seq104():
    send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
    send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 104")
    print('Sequence 104 played')

def MA3_Clear():
    send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")

def LaserSeq():
    l.LaserSequence()

def NeoPixelSeq():
    n.neopixelsequencestart()

def FullSeq():
    REA_JumpLaserMarker()
    MA3_Seq104()
    l.LaserSequence()
    REA_Stop()