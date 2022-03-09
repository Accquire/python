import threading
num = 0
def work1():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print(f'num is {num}')
def work2():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print(f'num is {num}')
if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'result is {num}')