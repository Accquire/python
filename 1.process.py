from multiprocessing import Process
def test():
    while True:
        print(2)
if __name__ == '__main__':
    p=Process(target=test)
    p.start()
    print(1)