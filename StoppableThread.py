

import threading
import time
import datetime
import utility



class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, n):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()
        self.n = n

    def stop(self):
        print("Terminazione del thread")
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        pass



class LoggerThread(StoppableThread):


    def write_log(self):  # definisce funzione del log dei dati

        for i in range(5):
            if not self.stopped():
                now = datetime.datetime.now()
                time.sleep(2)
                utility.my_glob(n)
                print(utility.gfib)
                log_string = "{:4} {}{}{}".format(self.n, str(now.isoformat()), " " * 10, utility.gfib)
                print(log_string)
                with open(file_local_path, "a") as f:
                        time.sleep(2)
                        f.write(log_string + "\n")
                        f.close()

            else:
                return

    def run(self):
        self.write_log()




import shutil
import os
from utility import *
from mount import mount, is_mounted
n = 0


class Copier(StoppableThread):
        def copier(self):
            logger = None

            if not (logger and logger.is_alive()):
                    logger = LoggerThread(n)
                    logger.start()

                    print(devices)
                    if devices:  # controlla se c'e' la chiavetta
                        device = devices[0]
                        path_chiavetta = get_media_path(device)
                        mount(device)  #monta la chiavetta
                        print("DEVICE EXISTS")


                        if is_mounted(device): #controlla se e' montata la usb
                            if logger.is_alive():
                                print("Salvataggio su chiavetta")
                                logger.join()
                                logger.stop()
                                shutil.copy2(file_local_path, path_chiavetta)      #copia il file da locale a chiavetta
                                os.remove(file_local_path) #dove va messo, cancellerebbe il file da locale
                            else:
                                pass
                        else:
                            pass

                    else:
                        logger.join()
                        print("MAREMMA CANE non vede la chiavetta")


        def run(self):
            self.copier()