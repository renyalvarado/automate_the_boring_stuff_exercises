#! /usr/bin/env python3
# Stopwatch
import time

print("Press ENTER to begin. Afterward, press Enter to 'click' the stopwatch")
input()
print("Started.")
start_time = time.time()
last_time = start_time
lap_number = 1
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap #{lap_number}: {total_time} {lap_time}")
        lap_number += 1
        last_time = time.time()
except KeyboardInterrupt:
    print("\nDone!")
