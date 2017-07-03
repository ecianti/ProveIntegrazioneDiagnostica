import time
fibbone = 0
i = 0
from utility import my_fib
for i in range(10000):
    i += 1
    fibbone = my_fib(i)
    print("bestemmia n = " + str(fibbone))
    time.sleep(1)
