from threading import Thread
def work1():
    while True:
        pass
def work2():
    while True:
        pass
if __name__ == '__main__':
    t1 = Thread(target=work1)
    t1.start()
    t2 = Thread(target=work2)
    t2.start()