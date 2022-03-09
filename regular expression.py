import re
def test1():
    list1= ['bat','bit', 'but', 'hat', 'hit', 'hut']
    for i in list1:
        result = re.match('[a-z]+t$',i)
        print(result.group())

def test2():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for j in email_list:
        result = re.match('[\w]{4,20}@163\.com$',j)
        if result:
            print('result.group()')
        else:
            print(f'{j} is not a email')

def test3():
    ret = re.match("[1-9]?[0-9]", "7")
    print(ret.group())
    ret = re.match("[1-9]?\d", "33")
    print(ret.group())
    ret = re.match("[1-9]?\d$", "09")
    if ret:
        print(ret.group())
    else:
        print('match is error')

if __name__ == '__main__':
    test3()