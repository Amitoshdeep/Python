import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up the keyboard
keyboard = Keyboard(usb_hid.devices)

# Wait for a moment to ensure the computer is ready
time.sleep(2)

# Open the terminal (different commands for different OS)
# Windows: Win + R, type "cmd", Enter
keyboard.press(Keycode.WINDOWS)
keyboard.release_all()
time.sleep(0.5)
keyboard.send(Keycode.R)
time.sleep(0.5)
keyboard.release_all()

# Type "cmd" and press Enter
keyboard.send(Keycode.C, Keycode.M, Keycode.D)
time.sleep(0.5)
keyboard.send(Keycode.ENTER)

# Wait for the terminal to open
time.sleep(1)

# Define the name to type
name = "AMITOSHDEEP"

# Type each character with a delay
for char in name:
    # Use SHIFT for uppercase letters
    if char.isupper():
        keyboard.press(Keycode.SHIFT)  # Hold down SHIFT
        keyboard.send(getattr(Keycode, char))  # Send the character as uppercase
        keyboard.release(Keycode.SHIFT)  # Release SHIFT
    else:
        # For lowercase, simply send the key
        keyboard.send(getattr(Keycode, char.upper()))
    time.sleep(0.1)  # 100ms delay between each character
keyboard.send(Keycode.ENTER)