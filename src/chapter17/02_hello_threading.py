#! /usr/bin/env python3
# Using Threads
import threading
import time

print('Start of program.')


def sleeping():
    time.sleep(5)
    print('Wake up!')


thread_obj = threading.Thread(target=sleeping)
thread_obj.start()

thread_obj2 = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
thread_obj2.start()


print('End of program.')
