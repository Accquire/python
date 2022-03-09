import threading
import time
def work1():
    a.acquire()
    time.sleep(1)
    b.acquire()
    b.release()
    a.release()
def work2():
    b.acquire()
    time.sleep(1)
    a.acquire()
    a.release()
    b.release()
if __name__ == '__main__':
    a = threading.Lock()
    b = threading.Lock()
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()