from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime

lock = Lock()


class CleanOutputSet(set):
    def __str__(self):
        return ", ".join(x for x in self)


loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print("[" + str(ctime()) + "] Started " + str(myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print("[%s] Completed %s (%d secs)" % (ctime(), myname, nsec))
    print("  (remaining: %s)" % (remaining or "NONE"))
    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print("all DONE at: ", ctime())

if __name__ == "__main__":
    _main()

# Output:
# /usr/bin/python3.5 /root/PycharmProjects/MT/locking.py
# [Wed Jun 20 16:57:10 2018] Started Thread-1
# [Wed Jun 20 16:57:10 2018] Started Thread-2
# [Wed Jun 20 16:57:10 2018] Started Thread-3
# [Wed Jun 20 16:57:10 2018] Started Thread-4
# [Wed Jun 20 16:57:10 2018] Started Thread-5
# [Wed Jun 20 16:57:10 2018] Started Thread-6
# [Wed Jun 20 16:57:12 2018] Completed Thread-6 (2 secs)
#  (remaining: Thread-1, Thread-4, Thread-5, Thread-2, Thread-3)
# [Wed Jun 20 16:57:13 2018] Completed Thread-1 (3 secs)
#  (remaining: Thread-4, Thread-5, Thread-2, Thread-3)
# [Wed Jun 20 16:57:13 2018] Completed Thread-3 (3 secs)
#  (remaining: Thread-4, Thread-5, Thread-2)
# [Wed Jun 20 16:57:13 2018] Completed Thread-4 (3 secs)
#  (remaining: Thread-5, Thread-2)
# [Wed Jun 20 16:57:14 2018] Completed Thread-2 (4 secs)
#  (remaining: Thread-5)
# [Wed Jun 20 16:57:14 2018] Completed Thread-5 (4 secs)
#  (remaining: NONE)
# all DONE at:  Wed Jun 20 16:57:14 2018

# Process finished with exit code 0

