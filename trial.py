import threading
import time
import datetime
import utility
import os
import time
from StoppableThread import Copier
from mount import *
from utility import my_glob, gfib
from StoppableThread import n
file_local_path = "/home/stage/PycharmProjects/dir_thread/serie.txt"

k=0
devices = 0
device = 0


if devices:
    devices = list_media_devices()
    device = devices[0]
    path_chiavetta = get_media_path(device)
    mount(device)
else:
    print("i am the danger")



if is_mounted(device): #controlla se e' montata la usb

   for k in range(10):
       k += 1
       j = open(file_local_path, "a")
       j.write(my_glob(n))
       j.close()