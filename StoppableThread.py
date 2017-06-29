

import threading
import time
import datetime
from utility import gfib, file_local_path, path_chiavetta



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

import shutil

class LoggerThread(StoppableThread):



    def write_log(self):  # definisce funzione del log dei dati

        for i in range(5):
            if not self.stopped():
                now = datetime.datetime.now()
                time.sleep(2)
                log_string = "{:4} {}{}{}".format(self.n, str(now.isoformat()), " " * 10, gfib)
                print(log_string)
                with open(file_local_path, "a") as f:
                        time.sleep(2)
                        f.write(log_string)
                        f.close()

            else:
                return

    def run(self):
        self.write_log()

class Copier(StoppableThread):

    def __init__(self, n):

        super().__init__(n)
        self.os = None
        self.shutil = None

    def copier(self):
        self.shutil.copy2(file_local_path, path_chiavetta)      #copia il file da locale a chiavetta
        self.os.remove(file_local_path) #dove va messo, cancellerebbe il file da locale

