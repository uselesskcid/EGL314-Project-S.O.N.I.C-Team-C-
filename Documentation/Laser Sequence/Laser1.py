from pythonosc import udp_client
import tkinter as tk
import time
import Laser_DAW as DAW

# IP address and port of the receiving Raspberry Pi for lasers
PI_A_ADDR = "192.168.254.49"  # Change to your RPi's IP address
PORT = 2000

# Function to send color to NeoPixel
def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

# Function to send brightness to NeoPixel
def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

# Function to send UDP message
def send_message(receiver_ip, receiver_port, address, message):
    """Send a UDP message to the specified IP address and port."""
    # Simulating UDP message sending (replace with actual implementation)
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

# Activate left side lasers
def left_on():
    messages = [
        f"7, 1, 1", f"7, 2, 1",
        f"8, 1, 1", f"8, 2, 1",
        f"9, 1, 1", f"9, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate right side lasers
def right_on():
    messages = [
        f"1, 1, 1", f"1, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"3, 1, 1", f"3, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate front side lasers
def front_on():
    messages = [
        f"10, 1, 1", f"10, 2, 1",
        f"11, 1, 1", f"11, 2, 1",
        f"12, 1, 1", f"12, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate back side lasers
def back_on():
    messages = [
        f"4, 1, 1", f"4, 2, 1",
        f"5, 1, 1", f"5, 2, 1",
        f"6, 1, 1", f"6, 2, 1",
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate ribbon shape
def ribbon_shape_on():
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

# Activate plus shape
def plus_shape_on():
    messages = [
        f"11, 1, 1", f"11, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"5, 1, 1", f"5, 2, 1",
        f"8, 1, 1", f"8, 2, 1"
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate chase 1x1 shape
def chase1x1_on():
    messages = [
        f"1, 1, 1", f"1, 2, 1",
        f"2, 1, 1", f"2, 2, 1",
        f"3, 1, 1", f"3, 2, 1",
        f"4, 1, 1", f"4, 2, 1",
        f"5, 1, 1", f"5, 2, 1",
        f"6, 1, 1", f"6, 2, 1",
        f"7, 1, 1", f"7, 2, 1",
        f"8, 1, 1", f"8, 2, 1",
        f"9, 1, 1", f"9, 2, 1",
        f"10, 1, 1", f"10, 2, 1",
        f"11, 1, 1", f"11, 2, 1",
        f"12, 1, 1", f"12, 2, 1"
    ]
    for msg in messages:
        send_message(PI_A_ADDR, PORT, "/print", msg)

# Activate star shape
def star_shape_on():
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
        front_on()
        time.sleep(1)
        back_on()
        time.sleep(1)
        left_on()
        time.sleep(1)
        right_on()
        time.sleep(1)
        turn_off_all()
        time.sleep(1)

# GUI setup
root = tk.Tk()
root.title("Laser Control")

# Define buttons for each laser control action
btn_all_on = tk.Button(root, text="All On", command=turn_on_all)
btn_all_off = tk.Button(root, text="All Off", command=turn_off_all)
btn_left_on = tk.Button(root, text="Left On", command=left_on)
btn_right_on = tk.Button(root, text="Right On", command=right_on)
btn_front_on = tk.Button(root, text="Front On", command=front_on)
btn_back_on = tk.Button(root, text="Back On", command=back_on)
btn_ribbon_shape = tk.Button(root, text="Ribbon Shape", command=ribbon_shape_on)
btn_plus_shape = tk.Button(root, text="Plus Shape", command(plus_shape_on)
btn_chase1x1 = tk.Button(root, text="Chase 1x1", command=chase1x1_on)
btn_star_shape = tk.Button(root, text="Star Shape", command=star_shape_on)
btn_stop = tk.Button(root, text="Stop", command=stop)
btn_run_laser_show = tk.Button(root, text="Run Laser Show", command=run_laser_show)

# Place buttons in the GUI window
btn_all_on.pack()
btn_all_off.pack()
btn_left_on.pack()
btn_right_on.pack()
btn_front_on.pack()
btn_back_on.pack()
btn_ribbon_shape.pack()
btn_plus_shape.pack()
btn_chase1x1.pack()
btn_star_shape.pack()
btn_stop.pack()
btn_run_laser_show.pack()

# Start the GUI event loop
root.mainloop()
