import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Configuration
delay = 3  # Time between clicks
hold_duration = 0.5  # Duration to hold the button 
button = Button.left
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='k')

class ClickMouse(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = False
        self.program_running = True

    def run(self):
        while self.program_running:
            if self.running:
                mouse.press(button)  
                time.sleep(hold_duration)
                mouse.release(button)  
                time.sleep(delay)  
            time.sleep(0.1)  

# Initialize mouse controller and click thread
mouse = Controller()
click_thread = ClickMouse()
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        click_thread.running = not click_thread.running
        print("Auto-clicker", "started." if click_thread.running else "stopped.")
    elif key == exit_key:
        click_thread.program_running = False
        print("Exiting program...")
        return False

# Start the keyboard listener
with Listener(on_press=on_press) as listener:
    print("---- Dead by Daylight Bloodweb Auto-Clicker ----")
    print(f"Press '{start_stop_key.char}' to run, '{exit_key.char}' to kill.")
    listener.join()