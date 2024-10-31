import time
from pynput import mouse
import math
from pynput.mouse import Controller


mouse_movements = []
start_time = time.time()
time_set = int(input("Please enter runntime:"))


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
    if(time_set < 60):
        print(f"Recording mouse movements for {time_set} seconds...")
    else:
        print(f"Recording mouse movements for {round(time_set / 60, 2)} minutes...")
    listener.join()

mouse_controller = Controller()
print(f"\n{len(mouse_movements)} mouse movements were recorded.")
print("While replaying, please don't move your mouse.")

for position in mouse_movements:
    mouse_controller.position = position
    time.sleep(0.01)
if(time_set < 60):
    print(f"Replayed the last {time_set} seconds of your mouse")
else: 
    print(f"Replayed the last {time_set / 60} minutes of your mouse")
  
