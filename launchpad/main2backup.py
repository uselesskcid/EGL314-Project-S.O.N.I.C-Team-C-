import mido
import threading
import subprocess
import time

# Replace with your actual device name if different
midipad = 'Launchpad Pro MK3:Launchpad Pro MK3 LPProMK3 MIDI 28:0'

# Output port for sending commands
outport = mido.open_output(midipad)
# Input port for feedback from the launchpad
inport = mido.open_input(midipad)

def pixel(buttonid, colour):
    """Function to light up 1 pixel."""
    msg = mido.Message('note_on', note=buttonid, velocity=colour)
    outport.send(msg)

# Global variables to keep track of the running subprocess and mode
current_process = None
current_mode = None

def terminate_current_process():
    """Function to terminate the current process if it exists."""
    global current_process
    if current_process:
        print("Terminating current process...")
        current_process.terminate()
        current_process.wait()
        current_process = None
        print("Process terminated.")

def start_easy_mode():
    """Function to start easy mode."""
    global current_process, current_mode
    if current_mode != 'easy':  # Only start if not already in easy mode
        terminate_current_process()
        print("Starting easy mode...")
        current_process = subprocess.Popen(['python', 'easymode.py'])
        current_mode = 'easy'
        # Fill LEDs for easy mode
        

def start_hard_mode():
    """Function to start hard mode."""
    global current_process, current_mode
    if current_mode != 'hard':  # Only start if not already in hard mode
        terminate_current_process()
        print("Starting hard mode...")
        current_process = subprocess.Popen(['python', 'hardmode2.py'])
        current_mode = 'hard'
        # Clear the entire board and fill LEDs for hard mode
        clear_board()
        

def clear_board():
    """Function to clear the LED board."""
    for i in range(0, 128):
        pixel(i, 0)

press_count = 0
last_press_time = time.time()

def handle_midi_input():
    """Function to handle incoming MIDI messages."""
    global press_count, last_press_time
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity > 0:
            if msg.note == 54:
                if current_mode != 'hard':  # Only process if not in hard mode
                    current_time = time.time()
                    if current_time - last_press_time < 0.5:  # Adjust the time window as needed
                        press_count += 1
                    else:
                        press_count = 1
                    last_press_time = current_time
                    if press_count == 1:
                        threading.Timer(0.6, check_press_count).start()  # Delay slightly longer than the time window

def check_press_count():
    """Function to check the number of presses and start the appropriate mode."""
    global press_count
    if press_count == 1:
        start_easy_mode()
    elif press_count == 2:
        start_hard_mode()
    press_count = 0
    # Turn off the white light on button 54 if transitioning
    pixel(54, 0)

def start_midi_listener():
    """Function to run the MIDI input handler in a separate thread."""
    listener_thread = threading.Thread(target=handle_midi_input)
    listener_thread.daemon = True
    listener_thread.start()

if __name__ == "__main__":
    # Light up button 54 as white
    pixel(54, 127)  # 127 is usually the highest value for full brightness

    # Start listening for MIDI input
    start_midi_listener()

    # Keep the main thread alive
    while True:
        time.sleep(1)  # Prevent high CPU usage