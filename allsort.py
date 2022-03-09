import random
def bubble(arrlist):
    i = len(arrlist)-1
    while i >0:
        j = 0
        while j <len(arrlist)-1:
            if arrlist[j]>arrlist[j+1]:
                arrlist[j],arrlist[j+1]=arrlist[j+1],arrlist[j]
            j+=1
        i-=1
    print(arrlist)

def select(arrlist):
    i = 0
    while i <len(arrlist):
        min_pos = i
        j = i+1
        while j<len(arrlist):
            if arrlist[j]<arrlist[min_pos]:
                min_pos = j
            j+=1
        arrlist[i],arrlist[min_pos]=arrlist[min_pos],arrlist[i]
        i+=1
    print(arrlist)

def insert(arrlist):
    i = 1
    while i<len(arrlist):
        j = i-1
        while j >=0:
            if arrlist[i]<arrlist[j]:
                arrlist[j+1]=arrlist[j]
            else:
                break
            j-=1
        arrlist[j+1]=arrlist[i]
        i+=1
    print(arrlist)

def shell(arrlist):
    gap = len(arrlist)>>1
    while gap>0:
        i = gap
        while i <len(arrlist):
            j = i -gap
            insert_value=arrlist[i]
            while j>=0:
                if insert_value<arrlist[j]:
                    arrlist[j+gap]=arrlist[j]
                    j-=1
                else:
                    break
            arrlist[j+gap]=insert_value
            i+=1
        gap >>=1
    print(arrlist)

def partition(arrlist,left,right):
    i = left
    k = left
    while i<len(arrlist):
        if arrlist[i]<arrlist[right]:
            arrlist[i],arrlist[k]=arrlist[k],arrlist[i]
            k+=1
        i+=1
    arrlist[k],arrlist[right]=arrlist[right],arrlist[k]
    return k
def quick(arrlist,left,right):
    if left<right:
        pivot = partition(arrlist,left,right)
        quick(arrlist,left,pivot-1)
        quick(arrlist,pivot+1,right)
    else:
        print(arrlist)

def adjust_max_heap(arrlist,adjust_pos,arr_len):
    dad = adjust_pos
    son = dad*2+1
    while son<arr_len:
        if son+1<arr_len and arrlist[son+1]>arrlist[son]:
            son+=1
        if arrlist[son]>arrlist[dad]:
            arrlist[son],arrlist[dad]=arrlist[dad],arrlist[son]
            dad = son
            son = dad*2+1
        else:
            break
def heap(arrlist,arr_len):
    for i in range(arr_len//2-1,-1,-1):
        adjust_max_heap(arrlist,i,arr_len)
    arrlist[0],arrlist[arr_len-1]=arrlist[arr_len-1],arrlist[0]
    for i in range(arr_len-1,1,-1):
        adjust_max_heap(arrlist,0,i)
        arrlist[0],arrlist[i-1]=arrlist[i-1],arrlist[0]
    print(arrlist)

def count_sort(arrlist):
    maxsize = 101
    list1 = [0]*maxsize
    for i in arrlist:
        list1[i]+=1
    i = 0
    k = 0
    while i<maxsize:
        for j in range(list1[i]):
            arrlist[k] = i
            k+=1
        i+=1
    print(arrlist)

if __name__ == '__main__':
    list1 = []
    for i in range(13):
        list1.append(random.randint(0, 100))
    print(list1)
    bubble(list1)
    # select(list1)
    # insert(list1)
    # shell(list1)
    # quick(list1, 0, len(list1) - 1)
    heap(list1, len(list1))
    count_sort(list1)
