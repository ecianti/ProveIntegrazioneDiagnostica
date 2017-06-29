import time

from StoppableThread import LoggerThread, Copier
from mount import *
from utility import my_fib, gfib

n = 0
scrittura_in_locale = True
logger = None
varcopy = None
try:
    while True:
        n += 1
        x = my_fib(n)
        gfib = x
        time.sleep(1)
        devices = list_media_devices()
        time.sleep(1)
        #
        if scrittura_in_locale:
            if not (logger and logger.is_alive()):
                logger = LoggerThread(n)
                logger.start()
                scrittura_in_locale = False
        else:
            logger.join()
            print("Salvataggio su chiavetta")
            if devices:  # controlla se c'e' la chiavetta

                  device = devices[0]
                  path_chiavetta = get_media_path(device)
                  mount(device)  #monta la chiavetta

                  if is_mounted(device): #controlla se e' montata la usb
                      if logger.is_alive():
                          logger.stop()
                          varcopy = Copier(n)
                          varcopy.start()
            scrittura_in_locale = True

            if varcopy.is_alive():
                varcopy.stop()

            scrittura_in_locale = True
        #
        #     else:# se non c'e' la chiavetta continua a scrivere ciclicamente sul file locale
        #         pass
except KeyboardInterrupt:
    logger.stop()

'''
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