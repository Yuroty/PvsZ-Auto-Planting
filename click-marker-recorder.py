import time
from pynput import mouse, keyboard

clicks = []
mouse_listener = None

print("Switch to your game and press '2' to start recording...")

def wait_for_start(key):
    try:
        if key.char == '2':
            print("Starting recording...")
            return False
    except AttributeError:
        pass

with keyboard.Listener(on_press=wait_for_start) as listener:
    listener.join()

print("Recording clicks. Press '2' again to stop.")

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        clicks.append((x, y))
        print(f"Recorded click at ({x}, {y})")

def on_press(key):
    try:
        if key.char == '2':
            print("\nStop key pressed — saving clicks...")
            if mouse_listener is not None:
                mouse_listener.stop()
            return False
    except AttributeError:
        pass

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()

with open("markers.txt", "w") as f:
    f.write("clicks = [\n")
    for i, (x, y) in enumerate(clicks):
        end = ", " if i < len(clicks)-1 else ""
        f.write(f"({x}, {y}){end}\n")
    f.write("]\n")

print(f"Saved {len(clicks)} clicks to markers.txt. Exiting in 10 seconds...")
time.sleep(10)