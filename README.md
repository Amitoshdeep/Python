# Python

```markdown
# Raspberry Pi Pico 2 USB Keyboard Emulation

## Project Description

This project involves the Raspberry Pi Pico 2 programmed to emulate a USB keyboard. Upon connecting to a computer, the device opens a terminal (Command Prompt on Windows) and types the string "AMITOSHDEEP." The project showcases the capabilities of the Pico in interfacing with host systems through USB HID (Human Interface Device) protocols, demonstrating practical applications in automation and hardware-software interaction.

## Features
- Opens the terminal (Command Prompt) on Windows using the keyboard shortcut.
- Types a predefined string ("AMITOSHDEEP") automatically.
- Supports uppercase letters through the use of the `SHIFT` key.
- Utilizes MicroPython and the Adafruit HID library for keyboard emulation.

## Prerequisites

Before running this project, ensure you have the following:
- **Raspberry Pi Pico 2**.
- **Micro USB cable** for connecting the Pico to your computer.
- **MicroPython** installed on the Pico.
- **Adafruit HID library** for USB HID functionality.

## Installation

1. **Install MicroPython on the Raspberry Pi Pico 2**:
   - Download the latest MicroPython firmware for the Raspberry Pi Pico from the [official website](https://micropython.org/download/rp2-pico/).
   - Flash the firmware onto your Pico using a tool like `esptool.py`.

2. **Set Up the Adafruit HID Library**:
   - Download the Adafruit HID library from the [Adafruit CircuitPython HID library](https://circuitpython.org/libraries).
   - Copy the `adafruit_hid` folder into the `lib` directory of your Pico's filesystem.

3. **Upload the Code**:
   - Create a new file named `code.py` on your Pico and paste the following code:

   ```python
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
   ```

## Usage

1. Connect your Raspberry Pi Pico 2 to a USB port on your computer.
2. After a brief moment, the Pico will automatically open the Command Prompt and type "AMITOSHDEEP."
3. Ensure you have a text editor or command prompt open to observe the typed output.

## Important Notes
- This project is designed for Windows operating systems. For other OS (like macOS or Linux), the method for opening the terminal and the corresponding commands will need adjustments.
- Ensure that the necessary libraries are correctly installed on your Pico.
- You can modify the string to type by changing the `name` variable in the code.

## Acknowledgments

- Special thanks to Adafruit for providing the HID library and documentation that made this project possible.
- Thanks to the MicroPython community for their ongoing support and resources.

```

### Instructions for Usage
1. Create a new file named `README.md` in your project directory.
2. Copy and paste the content above into the file.
3. Save the file.

This `README.md` provides a clear overview of your project, including setup and usage instructions, which will help others understand and replicate your work. Let me know if you need any changes or additional sections!
```
