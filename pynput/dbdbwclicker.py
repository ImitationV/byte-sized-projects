import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 5
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
                mouse.click(button)
                time.sleep(delay)
            time.sleep(0.1)

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

with Listener(on_press=on_press) as listener:
    print("---- Dead by Daylight Bloodweb Auto-Clicker ----") 
    print(f"Press '{start_stop_key.char}' to run, '{exit_key.char}' to kill.")
    listener.join()

