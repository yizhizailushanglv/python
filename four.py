'''
def fountion(形式参数)：参数列表可以为空
['注释块'] 。。。可选
语句块
return[返回值]。。。可选
函数调用：函数名（实际参数)

def sum3(a,b,c):
    return a+b+c
print(sum3(1,2,3))
def pow3(x):
    return x**3
print(pow3(3))
print(sum3(pow3(1),pow3(2),pow3(3)))
print(pow3(1+2+3))

def myfun(a,b,c):#序列传参
    print('a=',a)
    print('b=',b)
    print('c=',c)
s1=[11,22,33]
s2=(1.1,2.2,3.3)
s3='ABC'
print(myfun(*s1))
print(myfun(*s2))
print(myfun(*s3))
#字典关键字传参，注意key和形参名字对应，不能多和不能少
d1={'c':33,'a':11,'b':22}
print(myfun(**d1))
#综合传参就是上面的混合

#不定长参数（可变参数）：星号元组形参，双星号字典形参
def myfun(*args):
    print('实参的个数是',len(args))
    print(args)
    i=1
    for x in args:
        print('第',i,'个参数是：',x)
        i=i+1
myfun(1,2)
print('-------------------')
myfun('100',200,'three',4.4)
print('---------------------------------------------------')
#双星号字典形参
def myfun2(**kwargs):
    print('参数个数',len(kwargs))
    for k,v in kwargs.items():
        print(k,':',v)
myfun2(name='midu',age=12)
print('--------------------------------------------------------------------------')
#注意形式参数*args后面还有普通参数，实际参数那里一定要c=5.。。。
def myfun3(a,*args,b,c):
    print(a,b,c,args)
myfun3(11,12,13,14,b=5,c=6)
#混合使用
def fn(a,b,*args,c,**kwargs):
    print(a,b,args,c,kwargs)

fn(1,2,11,12,13,c=14,d=15,e=16)
print('------------------------------------------------------------------------------------------------------')
'''
from functools import reduce

#函数也是个对象 和变量一样
'''''
def fn():
    print('hello world')
f1=fn()
print(f1)
'''
#----------------------------------------------------------------------------
'''map函数(func，*iterable):用函数func和可迭代对象iterable中的每个元素作为参数
计算出新的可迭代对象，当对端的一个可迭代对象完成迭代后，此迭代生成结束
def power(x):
    return x**2
#生成一个迭代器，此迭代器可以生成1到9自然数的平方
mit=map(power,range(1,10))
for x in mit:
    print(x,end='')
    ----------------------------------------------------------------------
reduce函数

def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5]))
----------------------------------------------------------------------
filter函数
filter(function or none,iterable)
''''''
def is_odd(n):
    return n%2==1
newlist=filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
print(newlist)
'''
#lambda表达式(匿名函数):创建一个匿名函数对象，同def类似，但不提供函数名
#语法：lambda[参数1，参数2，。。。]：表达式
#     中括号可以省略,例如：

def myadd (x,y):
    return x+y
#可以写成
myadd=lambda x,y:x+y
print("20+30",myadd(20,30))
print('-------------------------------------------------------------------------------------------------')
#装饰器
def deco(fn):
    print('装饰器函数被调用，返回原函数')
    return fn
@deco
def myfunc():
    print('函数myfunc被调用')
myfunc=deco(myfunc)



