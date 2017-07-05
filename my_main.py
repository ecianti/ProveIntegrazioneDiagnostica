import time
from StoppableThread import Copier
from StoppableThread import Fibo
from mount import *
from utility import  gfib, n
from StoppableThread import n
varcopy = None
varFib = None


try:

    #while True:
    varFib = Fibo()
    varFib.start()
    varFib.join()
     # settaggio variabile globale
    #time.sleep(1)
    #devices = list_media_devices()
    #time.sleep(1)
    varcopy = Copier()
    varcopy.start()
    varcopy.join()
    #if varcopy.is_alive():
    #    varcopy.stop()
    #    print("stop copier")

    #
    #     else:# se non c'e' la chiavetta continua a scrivere ciclicamente sul file locale
    #         pass
except KeyboardInterrupt as e:
    print(e.message)
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