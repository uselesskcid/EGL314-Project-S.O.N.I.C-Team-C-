from pythonosc import udp_client
import time
from threading import Thread
import random

# Define the OSC server IPs and ports
TRUSS_IP = "192.168.254.242"  # 242, 2005
TRUSS_PORT = 2005

BALLOON_IP = "192.168.254.102"  # 102, 2006
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
    send_brightness_balloon(0.05)
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

def gradual_balloon(NUM_PIXELS):
    step_delay = 6 / NUM_PIXELS
    for i in range(NUM_PIXELS + 1):  # Include the final state where all pixels are on
        colors = [(0, 0, 255) if j < i else (0, 255, 0) for j in range(NUM_PIXELS)]
        send_color_array_truss(colors)
        time.sleep(step_delay)


def meteor_effect(NUM_PIXELS, duration, speed, meteor_size):
    end_time = time.time() + duration
    position = 0
    
    while time.time() < end_time:
        # Create meteor effect
        colors = [(255, 255, 0)] * NUM_PIXELS
        for i in range(position, position + meteor_size):
            if i < NUM_PIXELS:
                colors[i] = (0, 0, 255)  # Purple color
        
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

def sparkling_effect(NUM_PIXELS, duration, brightness=0.5):
    send_brightness_balloon(brightness)
    end_time = time.time() + duration

    while time.time() < end_time:
        colors = [(0, 0, 0)] * NUM_PIXELS  # Start with all pixels off
        
        # Randomly light up approximately half of the pixels
        for i in random.sample(range(NUM_PIXELS), NUM_PIXELS // 2):
            colors[i] = random.choice([
                (0, 0, 255),  # Blue
                (0, 255, 0),  # Green
                (0, 255, 255),  # Cyan
                (255, 255, 0),  # Yellow
                (255, 0, 255)   # Magenta
            ])
        
        send_color_array_balloon(colors)
        time.sleep(0.1)  # Adjust the speed of sparkling as needed

def interpolate_color(color1, color2, factor):
    """Interpolate between two RGB colors by a factor between 0 and 1."""
    return (
        int(color1[0] + (color2[0] - color1[0]) * factor),
        int(color1[1] + (color2[1] - color1[1]) * factor),
        int(color1[2] + (color2[2] - color1[2]) * factor)
    )

def sparkling_effect_gradual(NUM_PIXELS, duration, brightness=0.5, speed=0.1):
    send_brightness_balloon(brightness)
    end_time = time.time() + duration

    # Define a list of colors to transition through
    color_palette = [
        (0, 0, 255),   # Blue
        (0, 255, 0),   # Green
        (0, 255, 255), # Cyan
        (255, 255, 0), # Yellow
        (255, 0, 255)  # Magenta
    ]
    
    current_color_index = 0
    next_color_index = 1
    transition_duration = 1.0  # Duration to transition from one color to the next

    while time.time() < end_time:
        colors = [(0, 0, 0)] * NUM_PIXELS  # Start with all pixels off
        
        elapsed_time = time.time() % transition_duration
        factor = elapsed_time / transition_duration
        
        # Interpolate between current and next color
        current_color = interpolate_color(
            color_palette[current_color_index],
            color_palette[next_color_index],
            factor
        )
        
        # Randomly light up approximately half of the pixels with the interpolated color
        for i in random.sample(range(NUM_PIXELS), NUM_PIXELS // 2):
            colors[i] = current_color
        
        send_color_array_balloon(colors)
        time.sleep(speed)  # Adjust the speed of sparkling as needed
        
        # Check if it's time to switch to the next color in the palette
        if elapsed_time >= transition_duration:
            current_color_index = (current_color_index + 1) % len(color_palette)
            next_color_index = (current_color_index + 1) % len(color_palette)

def gradual_stop(NUM_PIXELS, stop_duration=5):
    """Gradually turn off the NeoPixels."""
    step_delay = stop_duration / NUM_PIXELS
    for i in range(NUM_PIXELS, -1, -1):  # Start with all pixels on, and turn them off
        colors = [(0, 0, 0) if j >= i else (255, 255, 255) for j in range(NUM_PIXELS)]
        send_color_array_truss(colors)
        send_color_array_balloon(colors)
        time.sleep(step_delay)
    
    # Ensure all lights are off at the end
    send_off_truss()
    send_off_balloon()

def neopixelsequencestart():
    try:
        # Configuration
        NUM_PIXELS_TRUSS = 170  # Adjusted to 170 pixels for Truss
        NUM_PIXELS_BALLOON = 101  # Adjusted to 101 pixels for Balloon
        Riser_Duration = 28.5  # Duration of Riser Effect
        Blink_Duration = 26  # Duration of Blinking Sequence
        Gradual_Stop_Duration = 5  # Duration of Gradual Stop Effect
        send_brightness_truss(0.5)

        print('Neopixel Running')

        # 1. Gradual rise on Truss NeoPixels (Duration: 29 seconds)
        gradual_on(NUM_PIXELS_TRUSS, Riser_Duration)

        # 2. Balloon NeoPixels sparkling effect while Truss blinks sequences
        meteor_thread = Thread(target=sparkling_effect_gradual, args=(NUM_PIXELS_BALLOON, Blink_Duration + Gradual_Stop_Duration))
        meteor_thread.start()

        # Truss blinking sequences for 26 seconds
        red_blink_thread = Thread(target=red_blink_sequence, args=(NUM_PIXELS_TRUSS, 7.5))
        red_blink_thread.start()

        time.sleep(6)
        green_blink_thread = Thread(target=green_blink_sequence, args=(NUM_PIXELS_TRUSS, 7.5))
        green_blink_thread.start()

        time.sleep(6)
        blue_blink_thread = Thread(target=blue_blink_sequence, args=(NUM_PIXELS_TRUSS, 7.5))
        blue_blink_thread.start()

        time.sleep(6)
        purple_blink_thread = Thread(target=purple_blink_sequence, args=(NUM_PIXELS_TRUSS, 5.5))
        purple_blink_thread.start()

        # 3. Gradual stop of both Truss and Balloon NeoPixels (last 5 seconds)
        time.sleep(9)
        gradual_stop(NUM_PIXELS_TRUSS, 2.5)
        time.sleep(1)
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