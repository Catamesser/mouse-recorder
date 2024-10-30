import time
from tkinter import simpledialog
from pynput import keyboard, mouse
from pynput.mouse import Controller
import tkinter as tk
from tkinter import messagebox


mouse_movements = []
start_time = time.time()
root = tk.Tk()
root.withdraw()
time_set = simpledialog.askinteger("Input", "Please enter runntime:")

def on_move(x, y):
    global mouse_movements
    current_time = time.time()
    if current_time - start_time <= time_set:
        mouse_movements.append((x, y))
        if x < 1920:
            print("First monitor")
        else:
            print("Second monitor")
    else:
        return False


with mouse.Listener(on_move=on_move) as listener:
    print(f"Recording mouse movements for {time_set} seconds...")
    listener.join()

mouse_controller = Controller()
print(f"\n{len(mouse_movements)} mouse movements were recorded.")
print("While replaying, please don't move your mouse.")

for position in mouse_movements:
    mouse_controller.position = position
    time.sleep(0.01)
messagebox.showinfo("Alert ig...",f"Replayed the last {time_set} seconds of your mouse")

