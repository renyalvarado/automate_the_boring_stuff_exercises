#! /usr/bin/env python3
# Testing automation with PyAutoGui
import sys
import time
import pyautogui

time.sleep(8)
print("Testing automation with PyAutoGui")
#
# Moving mouse absolute
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

pyautogui.moveTo(500, 500, duration=0.25)
# Moving mouse relative
for i in range(10):
    pyautogui.move(100, 0, duration=0.25)
    pyautogui.move(0, 100, duration=0.25)
    pyautogui.move(-100, 0, duration=0.25)
    pyautogui.move(0, -100, duration=0.25)

pyautogui.rightClick(500, 500)
try:
    pyautogui.click("blocker_button.png")
except TypeError:
    print(f"Your are not using Google Chrome + AdBlock disabled")

pyautogui.click(500, 80)
pyautogui.write("Hello world!")
pyautogui.alert("Hello world2!")