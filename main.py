import time
from StoppableThread import Copier
from mount import *
from utility import  my_pane, gfib
from StoppableThread import n

varcopy = None

try:
    while True:
        n += 1
        my_pane(n)
        print(gfib)
        time.sleep(1)
        devices = list_media_devices()
        time.sleep(1)
        varcopy = Copier(n)
        varcopy.start()
        varcopy.join()
        if varcopy.is_alive():
            varcopy.stop()


        #
        #     else:# se non c'e' la chiavetta continua a scrivere ciclicamente sul file locale
        #         pass
except KeyboardInterrupt:
    varcopy.stop()

''' SCRITTURA IN R+
            x = open(file_local_path, "r+")
            for j in range(100):
          
          3       x.write("Ciao" + str(j))
            scrittura_in_locale = False
        x.close()


       unThread = Thread(target=write_log, )
           unThread.start()
          scrittura_in_locale = False
         gfib = x
 f.close()

'''