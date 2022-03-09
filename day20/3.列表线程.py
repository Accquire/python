from threading import Thread
def work1(list_a):
    list_a.append(4)
    print(list_a)
def work2(list_a):
    print(list_a)
if __name__ == '__main__':
    a = [1,2,3]
    t1 = Thread(target=work1,args=(a,))
    t2 = Thread(target=work2,args=(a,))
    t1.start()
    t2.start()