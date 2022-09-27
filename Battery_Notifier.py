## v01
import os
import psutil
import platform
import win10toast
from win10toast import ToastNotifier
from time import sleep

toaster = ToastNotifier()

def Alert(title, msg, duration = 10):
    if platform.system() == 'Windows':
        toaster.show_toast(title, msg, duration = duration)
    
while True:
    percent = psutil.sensors_battery().percent

    if percent <= 33:
        msg = 'The battery is draining, Its time to feed he machine.'
        Alert('Baterry Alert', msg)

        print('Battery Remaining', str(percent) + '%')
        sleep(1)
        os.system("clear || cls")
