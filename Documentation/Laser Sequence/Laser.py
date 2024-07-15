from pythonosc import udp_client
import tkinter as tk
import time
import Laser_DAW as DAW

# IP address and port of the receiving Raspberry Pi for lasers
PI_A_ADDR = "192.168.254.49"  # Change to your RPi's IP address
PORT = 2000

#NEOPIXEL
def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

# Function to send UDP message
def send_message(receiver_ip, receiver_port, address, message):
    """Send a UDP message to the specified IP address and port."""
    # Simulating UDP message sending (replace with actual implementation)
    print(f"Message '{message}' sent to {address}.")

#Reaper DAW stop
def stop():
        turn_off_all
        DAW.REA_Stop

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

# Activate Left ON
def left_ON():
    messages = [
        f"7, 1, 1", f"7, 2, 1",
        f"8, 1, 1", f"8, 2, 1",
        f"9, 1, 1", f"9, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate Right ON
def right_ON():
    messages = [
        f"1, 1, 1", f"1, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"3, 1, 1", f"3, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate lFront ON
def front_ON():
    messages = [
        f"10, 1, 1", f"10, 2, 1",
        f"11, 1, 1", f"11, 2, 1",
        f"12, 1, 1", f"12, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate Back ON
def back_ON():
    messages = [
        f"4, 1, 1", f"4, 2, 1",
        f"5, 1, 1", f"5, 2, 1",
        f"6, 1, 1", f"6, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate ribbon shape ON
def ribbon_shape_ON():
    messages = [
        f"1, 1, 1", f"1, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"3, 1, 1", f"3, 2, 1",
        f"7, 1, 1", f"7, 2, 1",
        f"8, 1, 1", f"8, 2, 1",
        f"9, 1, 1", f"9, 2, 1"
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate + shape ON
def plus_shape_ON():
    messages = [
        f"11, 1, 1", f"11, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"5, 1, 1", f"5, 2, 1",
        f"8, 1, 1", f"8, 2, 1"
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate X shape ON
def chase1x1_ON():
    messages = [
        f"1,1,1", f"1,2,1",
        f"2,1,1", f"2,2,1",
        f"3,1,1", f"3,2,1",
        f"4,1,1", f"4,2,1",
        f"5,1,1", f"5,2,1",
        f"6,1,1", f"6,2,1",
        f"7,1,1", f"7,2,1",
        f"8,1,1", f"8,2,1",
        f"9,1,1", f"9,2,1",
        f"10,1,1", f"10,2,1",
        f"11,1,1", f"11,2,1",
        f"12,1,1", f"12,2,1"
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate star shape ON
def star_shape_ON():
    messages = [
        f"11, 1, 1", f"11, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"4, 1, 1", f"4, 2, 1",
        f"6, 1, 1", f"6, 2, 1",
        f"8, 1, 1", f"8, 2, 1"
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Function to run the laser show sequence for 30 seconds
def run_laser_show():
    DAW.REA_JumpLaserMarker()
    start_time = time.time()
    while time.time() - start_time < 30:
        # Chase 3x3
        front_ON
        time.sleep(1)
        turn_off_all
        right_ON
        time.sleep(1)
        turn_off_all
        back_ON
        time.sleep(1)
        turn_off_all
        left_ON
        time.sleep(1)
        turn_off_all
        time.sleep(0.5)
        turn_on_all
        time.sleep(0.5)
        turn_off_all

        # Ribbon shape
        ribbon_shape_ON
        time.sleep(1)
        turn_off_all

        # Plus shape
        plus_shape_ON
        time.sleep(1)
        turn_off_all

        # Chase 1x1 shape
        chase1x1_ON()
        time.sleep(1)
        turn_off_all

        # Star shape
        star_shape_ON
        time.sleep(1)
        turn_off_all

        # Left side
        left_ON()
        time.sleep(0.5)
        turn_off_all()

        # Right side
        right_ON()
        time.sleep(0.5)
        turn_off_all()

        # Front side
        front_ON()
        time.sleep(0.5)
        turn_off_all()

        # Back side
        back_ON()
        time.sleep(0.5)
        turn_off_all()

        # After 30 seconds, turn off all lasers
        turn_off_all()
        stop()

# GUI setup
root = tk.Tk()
root.title("Laser Show Controller")

# Button to start the laser show
start_show_button = tk.Button(root, text="Start Laser Show", command=run_laser_show)
stop_button = tk.Button(root, text="Stop", command=stop)
start_show_button.pack(pady=10)
stop_button.pack(pady=10)

# Main loop for the GUI
root.mainloop()