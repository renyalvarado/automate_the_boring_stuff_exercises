#! /usr/bin/env python3
# Spiral Draw

import time
import pyautogui

print("Spiral Draw")

time.sleep(8)
pyautogui.click()
distance = 300
change = 20

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.25)  # Move Right
    distance -= change
    pyautogui.drag(0, distance, duration=0.25)  # Move Down
    pyautogui.drag(-distance, 0, duration=0.25)  # Move left
    distance -= change
    pyautogui.drag(0, -distance, duration=0.25)  # Move Up
