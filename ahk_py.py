import keyboard
import pyautogui
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import threading
import sys

def do_this_thing():
    pyautogui.hotkey('ctrl', 'l') # Send the CTRL + L keypress
    print("CTRL + L was pressed") # print message

def on_quit(icon, item):
    icon.stop()
    try:
        sys.exit()
    except SystemExit:
        pass  # Prevent the exception from propagating


def create_image():
    # Create an icon image for the system tray (16x16 px)
    image = Image.new('RGB', (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((8, 8, 56, 56), outline="black", fill="blue")
    return image

def hotkey_listener():
    while True:
        keyboard.wait('F1')
        do_this_thing()

def setup_tray():
    # Create a system tray icon with a quit option
    icon = pystray.Icon("AutoHotkey Simulation")
    
    # Create the image for the system tray icon
    image = create_image()
    
    # Create the menu with a "Quit" option
    icon.menu = pystray.Menu(item('Quit', on_quit))
    
    icon.icon = image
    icon.title = "AutoHotkey Simulation"
    
    # Run the icon in a separate thread
    icon.run()

# Run the hotkey listener in a separate thread
hotkey_thread = threading.Thread(target=hotkey_listener, daemon=True)
hotkey_thread.start()

# Setup the system tray icon
setup_tray()
