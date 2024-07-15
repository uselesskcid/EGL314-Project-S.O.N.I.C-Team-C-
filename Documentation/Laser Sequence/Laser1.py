from pythonosc import udp_client
import tkinter as tk
import time
import Laser_DAW as DAW

# IP address and port of the receiving Raspberry Pi for lasers
PI_A_ADDR = "192.168.254.49"  # Change to your RPi's IP address
PORT = 2000

# Function to send UDP message
def send_message(receiver_ip, receiver_port, address, message):
    """Send a UDP message to the specified IP address and port."""
    print(f"Message '{message}' sent to {address}.")

# Reaper DAW stop
def stop():
    turn_off_all()
    DAW.REA_Stop()

# Turn off lasers for all speakers
def turn_off_all():
    messages = [
        f"3, 2, 0", f"3, 1, 0",
        f"2, 1, 0", f"2, 2, 0",
        f"1, 2, 0", f"1, 1, 0",
        f"4, 2, 0", f"4, 1, 0",
        f"5, 1, 0", f"5, 2, 0",
        f"6, 2, 0", f"6, 1, 0",
        f"7, 2, 0", f"7, 1, 0",
        f"8, 1, 0", f"8, 2, 0",
        f"9, 2, 0", f"9, 1, 0",
        f"10, 1, 0", f"10, 2, 0",
        f"11, 1, 0", f"11, 2, 0",
        f"12, 2, 0", f"12, 1, 0",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Turn on lasers for all speakers
def turn_on_all():
    messages = [
        f"3, 2, 1", f"3, 1, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"1, 2, 1", f"1, 1, 1",
        f"4, 2, 1", f"4, 1, 1",
        f"5, 1, 1", f"5, 2, 1",
        f"6, 2, 1", f"6, 1, 1",
        f"7, 2, 1", f"7, 1, 1",
        f"8, 1, 1", f"8, 2, 1",
        f"9, 2, 1", f"9, 1, 1",
        f"10, 1, 1", f"10, 2, 1",
        f"11, 1, 1", f"11, 2, 1",
        f"12, 2, 1", f"12, 1, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Toggle lasers 1 to 6 on/off
def toggle_laser(laser_id, state):
    send_message(PI_A_ADDR, PORT, "/print", f"{laser_id}, 1, {state}")
    send_message(PI_A_ADDR, PORT, "/print", f"{laser_id}, 2, {state}")

def laser_1_on(): toggle_laser(1, 1)
def laser_1_off(): toggle_laser(1, 0)
def laser_2_on(): toggle_laser(2, 1)
def laser_2_off(): toggle_laser(2, 0)
def laser_3_on(): toggle_laser(3, 1)
def laser_3_off(): toggle_laser(3, 0)
def laser_4_on(): toggle_laser(4, 1)
def laser_4_off(): toggle_laser(4, 0)
def laser_5_on(): toggle_laser(5, 1)
def laser_5_off(): toggle_laser(5, 0)
def laser_6_on(): toggle_laser(6, 1)
def laser_6_off(): toggle_laser(6, 0)

# Function to run the laser show sequence for 30 seconds with beat variable
def run_laser_show():
    beat = 1  # Initialize beat counter
    DAW.REA_JumpLaserMarker()
    start_time = time.time()
    while time.time() - start_time < 30:
        print(f"Beat: {beat}")  # Print the current beat for debugging
        send_message(PI_A_ADDR, PORT, "/print", "1, 1, 1")
        time.sleep(1)
        send_message(PI_A_ADDR, PORT, "/print", "1, 1, 0")
        time.sleep(1)
        send_message(PI_A_ADDR, PORT, "/print", "2, 1, 1")
        time.sleep(1)
        send_message(PI_A_ADDR, PORT, "/print", "2, 1, 0")
        time.sleep(1)
        send_message(PI_A_ADDR, PORT, "/print", "3, 1, 1")
        time.sleep(1)
        send_message(PI_A_ADDR, PORT, "/print", "3, 1, 0")
        time.sleep(1)
        beat += 1  # Increment the beat counter
        turn_off_all()
        time.sleep(1)

# GUI setup
root = tk.Tk()
root.title("Laser Control")

# Improved Layout with a grid
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Define buttons for each laser control action
btn_all_on = tk.Button(frame, text="All On", command=turn_on_all)
btn_all_off = tk.Button(frame, text="All Off", command=turn_off_all)

btn_laser_1_on = tk.Button(frame, text="Laser 1 On", command=laser_1_on)
btn_laser_1_off = tk.Button(frame, text="Laser 1 Off", command=laser_1_off)
btn_laser_2_on = tk.Button(frame, text="Laser 2 On", command=laser_2_on)
btn_laser_2_off = tk.Button(frame, text="Laser 2 Off", command=laser_2_off)
btn_laser_3_on = tk.Button(frame, text="Laser 3 On", command=laser_3_on)
btn_laser_3_off = tk.Button(frame, text="Laser 3 Off", command=laser_3_off)
btn_laser_4_on = tk.Button(frame, text="Laser 4 On", command=laser_4_on)
btn_laser_4_off = tk.Button(frame, text="Laser 4 Off", command=laser_4_off)
btn_laser_5_on = tk.Button(frame, text="Laser 5 On", command=laser_5_on)
btn_laser_5_off = tk.Button(frame, text="Laser 5 Off", command=laser_5_off)
btn_laser_6_on = tk.Button(frame, text="Laser 6 On", command=laser_6_on)
btn_laser_6_off = tk.Button(frame, text="Laser 6 Off", command=laser_6_off)

btn_stop = tk.Button(frame, text="Stop", command=stop)
btn_run_laser_show = tk.Button(frame, text="Start Laser Sequence", command=run_laser_show)

# Place buttons in the GUI window using grid layout
btn_all_on.grid(row=0, column=0, padx=5, pady=5)
btn_all_off.grid(row=0, column=1, padx=5, pady=5)

btn_laser_1_on.grid(row=1, column=0, padx=5, pady=5)
btn_laser_1_off.grid(row=1, column=1, padx=5, pady=5)
btn_laser_2_on.grid(row=2, column=0, padx=5, pady=5)
btn_laser_2_off.grid(row=2, column=1, padx=5, pady=5)
btn_laser_3_on.grid(row=3, column=0, padx=5, pady=5)
btn_laser_3_off.grid(row=3, column=1, padx=5, pady=5)
btn_laser_4_on.grid(row=4, column=0, padx=5, pady=5)
btn_laser_4_off.grid(row=4, column=1, padx=5, pady=5)
btn_laser_5_on.grid(row=5, column=0, padx=5, pady=5)
btn_laser_5_off.grid(row=5, column=1, padx=5, pady=5)
btn_laser_6_on.grid(row=6, column=0, padx=5, pady=5)
btn_laser_6_off.grid(row=6, column=1, padx=5, pady=5)

btn_stop.grid(row=7, column=0, padx=5, pady=5)
btn_run_laser_show.grid(row=7, column=1, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()