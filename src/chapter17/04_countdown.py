#! /usr/bin/env python3
# Countdown
import pathlib
import subprocess
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

sound_file = pathlib.Path("sound/alarm.wav")
subprocess.Popen(["see", sound_file.absolute()])
