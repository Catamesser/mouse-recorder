# Mouse Movement Recorder and Replayer

This Python script records mouse movements for a specified duration and then replays those movements. It utilizes the `pynput` library to monitor mouse actions and the `tkinter` library for user input and alerts.

## Features

- Records mouse movements for a user-defined period.
- Distinguishes between two monitors based on mouse coordinates.
- Replays the recorded mouse movements after the recording period ends.
- Alerts the user when replaying is complete.

## Requirements

To run this script, you need to have Python installed along with the following libraries:

- `pynput`
- `tkinter` (comes pre-installed with Python)

You can install the required libraries using pip:

```bash
pip install pynput
```
1- Run the script like this:
python mouse_movement_recorder.py

2- A dialog box will appear prompting you to enter the runtime in seconds. Input the desired duration for recording mouse movements.

3- The script will start recording your mouse movements for the specified time. During this time, the console will display which monitor the mouse is on (either "First monitor" or "Second monitor").

4- After the specified time elapses, the recorded mouse movements will be replayed automatically.

5- A message box will pop up notifying you that the replay is complete.

Notes
Ensure that you do not move the mouse during the replay process, as it may disrupt the replay accuracy.
This script is intended for use in a dual-monitor setup, but it can be modified for single-monitor use if needed and even for laptop or monitors with higher resolutions than 1920.
Example
If you enter 5 for the runtime, the script will record your mouse movements for 5 seconds and then replay them.
