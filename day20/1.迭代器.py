from collections.abc import Iterable,Iterator
class MyList:
    def __init__(self):
        self.list=[]
    def add(self,elem):
        self.list.append(elem)
    def __iter__(self):
        ilist = Ilist(self)
        return ilist

class Ilist:
    def __init__(self, mylist):
        self.mylist: MyList = mylist
        self.current = 0

    def __next__(self):
        current = self.current
        self.current += 1
        if current < len(self.mylist.list):
            return self.mylist.list[current]
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist=MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    print(isinstance(mylist.list,Iterable))
    for i in mylist:
        print(i)