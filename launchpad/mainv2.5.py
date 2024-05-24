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
start_button_active = True  # Flag to track if the start button is active
mode_buttons_active = False  # Flag to track if mode buttons are active

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
        clear_board()
        light_mode_buttons()  # Ensure mode buttons remain lit

def start_hard_mode():
    """Function to start hard mode."""
    global current_process, current_mode
    if current_mode != 'hard':  # Only start if not already in hard mode
        terminate_current_process()
        print("Starting hard mode...")
        current_process = subprocess.Popen(['python', 'hardmode2.py'])
        current_mode = 'hard'
        clear_board()
        light_mode_buttons()  # Ensure mode buttons remain lit

def clear_board():
    """Function to clear the LED board."""
    for i in range(0, 128):
        pixel(i, 0)

def light_mode_buttons():
    """Function to light up the mode buttons."""
    pixel(17, 64)  
    pixel(18, 96)  
    


def handle_midi_input():
    """Function to handle incoming MIDI messages."""
    global start_button_active, mode_buttons_active
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity > 0:
            if msg.note == 54 and start_button_active:
                start_button_active = False
                mode_buttons_active = True
                pixel(54, 0)  # Turn off the LED for button 54
                start_easy_mode()  # Default to easy mode
                light_mode_buttons()  # Light up mode buttons
            elif msg.note == 18 and mode_buttons_active:
                start_hard_mode()
            elif msg.note == 17 and mode_buttons_active:
                start_easy_mode()

def start_midi_listener():
    """Function to run the MIDI input handler in a separate thread."""
    listener_thread = threading.Thread(target=handle_midi_input)
    listener_thread.daemon = True
    listener_thread.start()

if __name__ == "__main__":
    # Light up button 54 as white to indicate it's the start button
    pixel(54, 127)  # 127 is usually the highest value for full brightness

    # Start listening for MIDI input
    start_midi_listener()

    # Keep the main thread alive
    while True:
        time.sleep(1)  # Prevent high CPU usage