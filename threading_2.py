### Create thread instance passing in callable class instance ###

import threading
from time import sleep, ctime

loops = [4,2]

class ThreadFunc(object):

    def __init__(self, func, args, name=""):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print("Start loop", nloop, " at: ", ctime())
    sleep(nsec)
    print("loop", nloop, "done at: ", ctime())

def main():
    print ("Starting at: ", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:  # Create all threads
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:  # Start all threads
        threads[i].start()

    for i in nloops:  # wait for completion
        threads[i].join()

    print("All done at: ", ctime())


if __name__ == "__main__":
    main()
