from threading import Thread
def say_sorry():
    print('I am so sorry')

if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=say_sorry)
        t.start()