from pythonosc import udp_client
import time

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
MA3_IP = "192.168.254.229"		# NEW laptop IP
MA3_PORT = 8888 # GRANDMA3 Local listen port
MA3_ADDR = "/gma3/cmd" # Trigger TRUE Value
# msg = "Go Sequence wtv"


# REAPER SETTINGS RIGHT HERE
REA_IP = "192.168.254.30"		# laptop IP
REA_PORT = 6800 # REAPER Local listen port
REA_MSG = float(1) # Trigger TRUE Value
# addr = "/action"

# GRANDMA3 CODE SEQUENCE

def MA3_Seq91():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 91")
	print('Sequence 91 played')
	
def MA3_Seq92():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 92")
	print('Sequence 92 played')

def MA3_Seq93():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 93")
	print('Sequence 93 played')
	
def MA3_Seq94():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 94")
	print('Sequence 94 played')
	
def MA3_Seq95():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 95")
	print('Sequence 95 played')

def MA3_Seq96():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 96")
	print('Sequence 96 played')
	
def MA3_Seq97():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Go+: Sequence 97")
	print('Sequence 97 played')
	
def MA3_Clear():
	send_message(MA3_IP, MA3_PORT, MA3_ADDR, "Off MyRunningSequence")
	print('Sequence cleared')
	
# REAPER CODE SEQUENCE

def REA_JumpEasy(): #Marker 18
	send_message(REA_IP, REA_PORT, "/action/41258", REA_MSG)
	print('Marker 18 jumped')

def REA_JumpHard(): #Marker 9
	send_message(REA_IP, REA_PORT, "/action/40169", REA_MSG)
	print('Marker 9 jumped')

def REA_JumpWin(): #Marker 59 Timeline
	send_message(REA_IP, REA_PORT, "/marker/59", REA_MSG)
	print('Marker 59 jumped')

def REA_JumpLose(): #Marker 10
	send_message(REA_IP, REA_PORT, "/action/40160", REA_MSG)
	print('Marker 10 jumped')	

def REA_JumpSampleBeat(): #Marker 56 Timeline
	send_message(REA_IP, REA_PORT, "/marker/56", REA_MSG)
	print('Marker 56 jumped')

def REA_JumpSuspense(): #Marker 57 Timeline
	send_message(REA_IP, REA_PORT, "/marker/57", REA_MSG)
	print('Marker 57 jumped')

def REA_JumpBGM(): #Marker 58 Timeline
	send_message(REA_IP, REA_PORT, "/marker/58", REA_MSG)
	print('Marker 58 jumped')	

def REA_PlayPause(): #Play/Pause
	send_message(REA_IP, REA_PORT, "/action/40073", REA_MSG)
	print('Play/Pause')
	
# SEQUENCE CODE SEQUENCE (These are functions stacked to make 1 bigger function)

def SEQ_Intro():
	MA3_Seq92()
	REA_JumpBGM()
	REA_PlayPause()
	time.sleep(60)
	REA_PlayPause()

def SEQ_OrangeBtn():
	MA3_Seq91()
	REA_JumpSuspense()
	REA_PlayPause()
	time.sleep(10)
	REA_PlayPause()

def SEQ_Win():
	MA3_Seq97()
	REA_JumpWin()
	REA_PlayPause()
	time.sleep(6)
	REA_PlayPause()
	
def SEQ_Lose():
	MA3_Seq96()
	REA_JumpLose()
	REA_PlayPause()
	time.sleep(6)
	REA_PlayPause()