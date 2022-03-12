import re
def match_http():
    result = re.match(r'[^w]+w{3}\.[^.]+(\.com|\.edu|\.net)$','http://www.yahoo.edu')
    print(result.group())


def search_word():
    str2 = '啊哈哈啊哈哈啊哈哈啊哈zbc'
    result = re.search(r'[a-zA-Z]',str2)
    print(result.group())
    result = re.findall(r'[a-zA-Z]+',str2)
    print(result)

def search_num():
    str1 = '哈哈哈啊哈哈2333啊哈哈哈'
    result = re.search(r'\d',str1)
    print(result.group())
    result = re.findall(r'\d+',str1)
    print(result)


def match_nw():
    result = re.findall('\d+','52a6所开放时间565464')
    if result:
        result = re.findall('[a-zA-Z]+','52a6所开放时间565464')
        if result:
            print('该行文字合格')
        else:
            print('不合格文字行')
    else:
        print('不合格文字行')

def disapper():
    str1 = '''<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p> <br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p> <br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div> '''
    result = re.sub(r'<[^>]+>','',str1)
    print(result)

def match_http():
    list1= ['http://www.interoem.com/messageinfo.asp?id=35',
            'http://3995503.com/class/class09/news_show.asp?id=14',
            'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
            'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
            'http://www.fincm.com/newslist.asp?id=415']
    for i in list1:
        result = re.sub(r'.*[^/]//|/.*','',i)
        print(result)

def match_time():
    str1 ='今天是2020年3月10号,17时05分'
    result = re.sub('^[^\d]+|号|,|分',' ',str1)
    result = re.sub('年|月','/',result)
    result = re.sub('时',':',result)
    print(result)

def email():
    str1='fasfufhuishguhus@qq.com'
    result = re.sub('^[^@]+','154628144',str1)
    result = re.sub('[a-zA-Z]+','163',result)
    result = re.sub('\d+$','com',result)
    print(result)

def words():
    str1 = 'hello world ha ha'
    result = re.split(' ',str1)
    for i in result:
        print(i)
if __name__ == '__main__':
    # match_http()
    # search_num()
    # search_word()
    # match_nw()
    # disapper()
    # match_http()
    # words()
    # match_time()
    email()