from pythonosc import osc_server, dispatcher
from pythonosc import udp_client
import tkinter as tk
import B3S2_LaserReaper as reaper
import time

PI_B_ADDR = "192.168.254.242"  # Whose IP address is this?
PORT2 = 2005 # And whose port?

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)
		print("Message sent successfully.")

	except:
		print("Message not sent")

TeamA_Pi = "192.168.254.49"
TeamA_Port = 2000
Addr = "/print"

# =====================================  LASER DEFINITION SECTION ======================================= #
def EveryLaserOn():
    seq = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1", "4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1", "7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1", "10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def EveryLaserOff():
    seq = ["1,1,0", "1,2,0", "2,1,0", "2,2,0", "3,1,0", "3,2,0", "4,1,0", "4,2,0", "5,1,0", "5,2,0", "6,1,0", "6,2,0", "7,1,0", "7,2,0", "8,1,0", "8,2,0", "9,1,0", "9,2,0", "10,1,0", "10,2,0", "11,1,0", "11,2,0", "12,1,0", "12,2,0"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def SpeakersOuter():
    seq = ["1,1,1", "1,2,1", "3,1,1", "3,2,1","4,1,1", "4,2,1", "6,1,1", "6,2,1","7,1,1", "7,2,1", "9,1,1", "9,2,1,","10,1,1", "10,2,1", "12,1,1", "12,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def SpeakersInner():
    seq = ["2,1,1", "2,2,1","5,1,1", "5,2,1", "8,1,1", "8,2,1","11,1,1", "11,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def Speakers1to3_1by1():
    seq = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1"]
    
    x = int(0)
    while x < len(seq):
        send_message(TeamA_Pi, TeamA_Port, Addr, seq[x])
        print(seq[x])
        x += 1

        if x == len(seq):
            break

def Speakers4to6_1by1():
    seq = ["4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1"]
    
    x = int(0)
    while x < len(seq):
        send_message(TeamA_Pi, TeamA_Port, Addr, seq[x])
        print(seq[x])
        x += 1

        if x == len(seq):
            break

def Speakers7to9_1by1():
    seq = ["7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1"]
    
    x = int(0)
    while x < len(seq):
        send_message(TeamA_Pi, TeamA_Port, Addr, seq[x])
        print(seq[x])
        x += 1

        if x == len(seq):
            break

def Speakers10to12_1by1():
    seq = ["10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    
    x = int(0)
    while x < len(seq):
        send_message(TeamA_Pi, TeamA_Port, Addr, seq[x])
        print(seq[x])
        x += 1

        if x == len(seq):
            break
def SpeakersStar1():
    seq = ["2,1,1", "2,2,1", "4,1,1", "4,2,1", "12,1,1", "12,2,1", "7,1,1", "7,2,1", "9,1,1", "9,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def SpeakersStar2():
    seq = ["5,1,1", "5,2,1", "3,1,1", "3,2,1", "7,1,1", "7,2,1", "10,1,1", "10,2,1", "12,1,1", "12,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def SpeakersCross1():
    seq = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "7,1,1", "7,2,1", "9,1,1", "9,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def SpeakersCross2():
    seq = ["4,1,1", "4,2,1", "6,1,1", "6,2,1", "10,1,1", "10,2,1", "12,1,1", "12,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def Speakers1to3():
    seq = ["1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def Speakers4to6():
    seq = ["4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def Speakers7to9():
    seq = ["7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

def Speakers10to12():
    seq = ["10,1,1", "10,2,1", "11,1,1", "11,2,1", "12,1,1", "12,2,1"]
    send_message(TeamA_Pi, TeamA_Port, Addr, seq)

# ===================================== TEAM LASER SECTION ======================================= #
# Speaker Number, Laser Module, On/Off
# === On === #

def teamLaserOne_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 1, 1"])
	
def teamLaserTwo_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 2, 1"])
	
def teamLaserThree_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 1"])

def teamLaserFour_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 1"])
	
def teamLaserFive_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 1, 1"])
	
def teamLaserSix_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 2, 1"])

def teamAllLasers_On():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 1, 1"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 2, 1"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 1"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 1"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 1, 1"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 2, 1"])
	
# === Off === #

def teamLaserOne_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 1, 0"])
  
def teamLaserTwo_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 2, 0"])
  
def teamLaserThree_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 0"])

def teamLaserFour_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 0"])
  
def teamLaserFive_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 1, 0"])
  
def teamLaserSix_Off():
  send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 2, 0"])

def teamAllLasers_Off():
    send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 1, 0"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["1, 2, 0"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 1, 0"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["2, 2, 0"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 1, 0"])
    send_message(TeamA_Pi, TeamA_Port, Addr, ["3, 2, 0"])

# ===================================== LASER SEQUENCE SECTION ======================================= #

def LaserSequence():
    """send_color(PI_B_ADDR, PORT2, 255, 255, 0)  # change to ur choice of colour (255,255,255)
    send_brightness(PI_B_ADDR, PORT2, 0.3)   # change brightness (0-1)
    print("test")"""
    reaper.REA_JumpLaserMarker()
    BeatsPerMinute = 60/82 # Time interval between beats
    Counter = 0
    start_time = time.time()
    while time.time() - start_time < 30 :
        time.sleep(BeatsPerMinute)
        if Counter == 0:
            EveryLaserOff()
        if (Counter == 1):
            EveryLaserOn()
        if (Counter == 2):
            SpeakersOuter()
        if (Counter == 3):
            SpeakersInner()
        if (Counter == 4):
            EveryLaserOff()
        if (Counter == 5):
            SpeakersInner()
        if (Counter == 6):
            SpeakersOuter()
        if (Counter == 7):
            EveryLaserOff()
        if (Counter == 8):
            Speakers1to3_1by1()
        if (Counter == 9):
            Speakers7to9_1by1()
        if (Counter == 10):
            Speakers4to6_1by1()
        if (Counter == 11):
            Speakers10to12_1by1()
        if (Counter == 12):
            EveryLaserOff()
        if (Counter == 13):
            SpeakersCross1()
        if (Counter == 14):
            SpeakersCross2()
        if (Counter == 15):
            EveryLaserOff() 
        if (Counter == 16):
            SpeakersStar1()
        if (Counter == 17):
            EveryLaserOff()
            SpeakersStar2()
        if (Counter == 18):
            EveryLaserOff()
            SpeakersStar1()
        if (Counter == 19):
            EveryLaserOff    
            SpeakersStar2()
        if (Counter == 20):
            EveryLaserOff() 
        if (Counter == 21):
            SpeakersCross1()
        if (Counter == 22):
            EveryLaserOff()
            SpeakersCross2()
        if (Counter == 23):
            EveryLaserOff()
            SpeakersCross1()
        if (Counter == 24):
            EveryLaserOff()
            SpeakersCross2()
        if (Counter == 25):
            EveryLaserOff()
            SpeakersCross1()
        if (Counter == 26):
            EveryLaserOff()
            SpeakersCross2()
        if (Counter == 27):
            EveryLaserOff()
        if (Counter == 28):
            EveryLaserOn()
        if (Counter == 29):
            EveryLaserOff()
            Speakers1to3_1by1()
        if (Counter == 30):
            Speakers4to6_1by1()
        if (Counter == 31):
            Speakers7to9_1by1()
        if (Counter == 32):
            Speakers10to12_1by1()
        if (Counter == 31):
            EveryLaserOff()
            SpeakersCross1()
        if (Counter == 32):
            EveryLaserOff()
            SpeakersCross2()
        if (Counter == 33):
            EveryLaserOff()
            SpeakersStar1()
        if (Counter == 34):
            EveryLaserOff()
            SpeakersStar2()
        if (Counter == 35):
            EveryLaserOff()
            Speakers1to3()
        if (Counter == 36):
            EveryLaserOff()
            Speakers4to6()
        if (Counter == 37):
            EveryLaserOff()
            Speakers7to9()
        if (Counter == 38):
            EveryLaserOff()
            Speakers10to12()
        if (Counter == 39):
            EveryLaserOff()
            EveryLaserOn()
        if (Counter == 40):
            EveryLaserOff()
        print(Counter)
        Counter += 1

    EveryLaserOff()
    reaper.REA_Stop()
        
# ===================================== GUI SECTION ======================================= #

main = tk.Tk()
main.title("Laser GUI")
teamLabel=tk.Label(main,text="Team C Lasers", font="20")
teamLaserOne_On_Btn = tk.Button(main, text="Laser 1 On", bg="GREEN", width=20, height=4, command=teamLaserOne_On)
teamLaserTwo_On_Btn = tk.Button(main, text="Laser 2 On", bg="GREEN", width=20, height=4, command=teamLaserTwo_On)
teamLaserThree_On_Btn = tk.Button(main, text="Laser 3 On", bg="GREEN", width=20, height=4, command=teamLaserThree_On)
teamLaserFour_On_Btn = tk.Button(main, text="Laser 4 On", bg="GREEN", width=20, height=4, command=teamLaserFour_On)
teamLaserFive_On_Btn = tk.Button(main, text="Laser 5 On", bg="GREEN", width=20, height=4, command=teamLaserFive_On)
teamLaserSix_On_Btn = tk.Button(main, text="Laser 6 On", bg="GREEN", width=20, height=4, command=teamLaserSix_On)
teamAllLasers_On_Btn = tk.Button(main, text="All Lasers On", bg="GREEN", width=20, height=4, command=teamAllLasers_On)

teamLaserOne_Off_Btn = tk.Button(main, text="Laser 1 Off", bg="RED", width=20, height=4, command=teamLaserOne_Off)
teamLaserTwo_Off_Btn = tk.Button(main, text="Laser 2 Off", bg="RED", width=20, height=4, command=teamLaserTwo_Off)
teamLaserThree_Off_Btn = tk.Button(main, text="Laser 3 Off", bg="RED", width=20, height=4, command=teamLaserThree_Off)
teamLaserFour_Off_Btn = tk.Button(main, text="Laser 4 Off", bg="RED", width=20, height=4, command=teamLaserFour_Off)
teamLaserFive_Off_Btn = tk.Button(main, text="Laser 5 Off", bg="RED", width=20, height=4, command=teamLaserFive_Off)
teamLaserSix_Off_Btn = tk.Button(main, text="Laser 6 Off", bg="RED", width=20, height=4, command=teamLaserSix_Off)
teamAllLasers_Off_Btn = tk.Button(main, text="All Lasers Off", bg="RED", width=20, height=4, command=teamAllLasers_Off)

LaserSequenceStart_Btn = tk.Button(main, text="Laser Sequence GO", bg="YELLOW", fg="BLACK", width=40, height=4,command=LaserSequence)
Reaper_Start_Btn = tk.Button(main, text="Song Play", bg="PURPLE", width=20, height=4,command=reaper.REA_JumpLaserMarker)
Reaper_Stop_Btn = tk.Button(main, text="Song Stop", bg="PURPLE", width=20, height=4,command=reaper.REA_Stop)

teamLabel.grid(row=0, column=0, columnspan=2)
teamLaserOne_On_Btn.grid(row=1, column=0)
teamLaserTwo_On_Btn.grid(row=2, column=0)
teamLaserThree_On_Btn.grid(row=3, column=0)
teamLaserFour_On_Btn.grid(row=4, column=0)
teamLaserFive_On_Btn.grid(row=5, column=0)
teamLaserSix_On_Btn.grid(row=6, column=0)
teamAllLasers_On_Btn.grid(row=7, column=0)

teamLaserOne_Off_Btn.grid(row=1, column=1)
teamLaserTwo_Off_Btn.grid(row=2, column=1)
teamLaserThree_Off_Btn.grid(row=3, column=1)
teamLaserFour_Off_Btn.grid(row=4, column=1)
teamLaserFive_Off_Btn.grid(row=5, column=1)
teamLaserSix_Off_Btn.grid(row=6, column=1)
teamAllLasers_Off_Btn.grid(row=7, column=1)

LaserSequenceStart_Btn.grid(row=8, column=0, columnspan=2)
Reaper_Start_Btn.grid(row=9, column=0)
Reaper_Stop_Btn.grid(row=9, column=1)

main.mainloop()