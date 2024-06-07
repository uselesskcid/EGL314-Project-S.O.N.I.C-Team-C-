import tkinter as tk
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")
		
# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.104"		# laptop IP
PORT = 8000 # REAPER Local listen port
msg = "/gma3/cmd" # Trigger TRUE Value

def MA3_Seq91():
	send_message(PI_A_ADDR, PORT, "Go Sequence 91", msg)

def MA3_Seq92():
	send_message(PI_A_ADDR, PORT, "Go Sequence 92", msg)
	
def MA3_Seq93():
	send_message(PI_A_ADDR, PORT, "Go Sequence 93", msg)
	
def MA3_Seq94():
	send_message(PI_A_ADDR, PORT, "Go Sequence 94", msg)
	
def MA3_Seq95():
	send_message(PI_A_ADDR, PORT, "Go Sequence 95", msg)
	
def MA3_Seq96():
	send_message(PI_A_ADDR, PORT, "Go Sequence 96", msg)
	
def MA3_Seq97():
	send_message(PI_A_ADDR, PORT, "Go Sequence 97", msg)

main = tk.Tk()
main.title("Team C L-ISA Controller")

tabLabel=tk.Label(main,text="TEAM C GUI", font="20" )
Seq91Btn = tk.Button(main, text="Sequence 91", bg="GREEN",command=MA3_Seq91)
Seq92Btn = tk.Button(main, text="Sequence 92", bg="GREEN",command=MA3_Seq92)
Seq93Btn = tk.Button(main, text="Sequence 93", bg="GREEN",command=MA3_Seq93)
Seq94Btn = tk.Button(main, text="Sequence 94", bg="GREEN",command=MA3_Seq94)
Seq95Btn = tk.Button(main, text="Sequence 95", bg="GREEN",command=MA3_Seq95)
Seq96Btn = tk.Button(main, text="Sequence 96", bg="GREEN",command=MA3_Seq96)
Seq97Btn = tk.Button(main, text="Sequence 97", bg="GREEN",command=MA3_Seq97)

tabLabel.grid(row=0,column=0,columnspan=2)
Seq91Btn.grid(row=1,column=0)
Seq92Btn.grid(row=1,column=1)
Seq93Btn.grid(row=1,column=2)
Seq94Btn.grid(row=1,column=3)
Seq95Btn.grid(row=1,column=4)
Seq96Btn.grid(row=1,column=5)
Seq97Btn.grid(row=1,column=6)

main.mainloop()