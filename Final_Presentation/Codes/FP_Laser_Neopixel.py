from pythonosc import udp_client
import time
from threading import Thread

# Define the OSC server IPs and ports
TRUSS_IP = "192.168.254.242"  # Change to your Truss RPi's IP address
TRUSS_PORT = 2005

BALLOON_IP = "192.168.254.102"  # Change to your Balloon RPi's IP address
BALLOON_PORT = 2006

# Create OSC clients
truss_client = udp_client.SimpleUDPClient(TRUSS_IP, TRUSS_PORT)
balloon_client = udp_client.SimpleUDPClient(BALLOON_IP, BALLOON_PORT)

######################## Functions for Truss Neopixel ##########################
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


################### Functions for Balloon Neopixel ############################

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

def neopixelsequencestart():
    try:
        # Configuration
        NUM_PIXELS_TRUSS = 170  # Adjusted to 170 pixels for Truss
        NUM_PIXELS_BALLOON = 101  # Adjusted to 101 pixels for Balloon
        duration = 29  # Duration of Riser Effect.
        meteor_size = 15  # Size of the meteor effect
        meteor_speed = 0.03  # Speed of the meteor effect (faster)

        print('Neopixel Running')
        # Gradually turn on Truss NeoPixels over 29 seconds
        gradual_on(NUM_PIXELS_TRUSS, duration)

        # Turn off all NeoPixels after the gradual effect ends
        send_off_truss()
        send_off_balloon()
        

        # Start the meteor effect and final blinking sequence immediately after turning off
        meteor_duration = 7.5  # Duration for meteor effect and final blinking sequence
        meteor_thread = Thread(target=meteor_effect, args=(NUM_PIXELS_BALLOON, meteor_duration, meteor_speed, meteor_size))
        meteor_thread.start()

        # Final blinking sequence for Truss NeoPixels
        red_blink_thread = Thread(target=red_blink_sequence, args=(NUM_PIXELS_TRUSS, meteor_duration))
        red_blink_thread.start()

        time.sleep(6)
        green_blink_thread = Thread(target=green_blink_sequence, args=(NUM_PIXELS_TRUSS, meteor_duration))
        green_blink_thread.start()

        time.sleep(6)
        blue_blink_thread = Thread(target=blue_blink_sequence, args=(NUM_PIXELS_TRUSS, meteor_duration))
        blue_blink_thread.start()

        time.sleep(6)
        purple_blink_thread = Thread(target=purple_blink_sequence, args=(NUM_PIXELS_TRUSS, meteor_duration))
        purple_blink_thread.start()

        # Wait for both effects to finish
        meteor_thread.join()
        blue_blink_thread.join()

        # Turn off all NeoPixels after the effects are done
        send_off_truss()
        send_off_balloon()

    except KeyboardInterrupt:
        # Turn off all NeoPixels on exit
        send_off_truss()
        send_off_balloon()
        print("Client stopped")
    except Exception as e:
        print(f"Error: {e}")
        send_off_truss()
        send_off_balloon()