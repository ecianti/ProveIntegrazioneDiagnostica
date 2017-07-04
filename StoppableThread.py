import threading
import time
import datetime
import utility

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, ):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

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
                time.sleep(1)

                self.scrivi_file()

    def scrivi_file(self):
        Fibo().get_global_variable()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_string = "{}{}{}".format(str(now), " " * 10, Fibo().get_global_variable())
        print(log_string)
        with open(file_local_path, "a+") as f:
            f.write(log_string + "\n")
            time.sleep(2)
            f.close()

    def run(self):
        self.write_log()


import shutil
import os
from utility import *
from mount import mount, is_mounted

n = 0
x = 0


class Copier(StoppableThread):
    def copier(self):
        logger = None
        while True:
            logger = LoggerThread()
            logger.start()
            logger.join()
            devices = list_media_devices()

            if devices:  # controlla se c'e' la chiavetta
                self.copia_su_chiavetta(devices, logger)
                print("COPIATO")
            else:
                print("MAREMMA CANE non vede la chiavetta")

    def copia_su_chiavetta(self, devices, logger):
        device = devices[0]
        path_chiavetta = get_media_path(device)
        mount(device)  # monta la chiavetta
        print("DEVICE EXISTS")

        if is_mounted(device):  # controlla se e' montata la usb
            print("Salvataggio su chiavetta")
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            now = now.replace(":","").replace(" ", "T")
            new_file = os.path.join(path_chiavetta, now)
            shutil.copy2(file_local_path, new_file)  # copia il file da locale a chiavetta
            time.sleep(2)
            os.remove(file_local_path)  # dove va messo, cancellerebbe il file da locale

    def run(self):
        self.copier()


from utility import my_fib
class Fibo(StoppableThread):
    def get_global_variable(self):
        global gfib
        global n
        while True:
            print("incremento")
            n += 1
            gfib = my_fib(n)
            time.sleep(2)
            return gfib




