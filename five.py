#模块----------------------------------
import sys
import math,os
import datetime

from one import a
from two import b

#print(math.sin(3.14))
#print(datetime.datetime.now())
#from datetime import datetime as DT#从模块导出一个函数
#print(DT.now())
#print('-----------------------------------------------------------------------------------------')
from datetime import *   #全部导出模块内容
#自定义模块 ,模块也是对象
#包（模块包）其实就是一个分类，目录
'''
mypack/
__init__.py
menu.py
games/
    __init__.py
    contra.py
    supermario.py
    tanks.py
offic/
    __init__.py
    excel.py
    word.py
    powerpoint.py
    
'''
#包的调用和模块差不多，就是包里面不能。包 即包.包是不对的#

                   #类 class 类的创建语法 class也是对象
#class 类名（继承列表）
  #‘类文档字符串’
 # 实例方法（类内的函数method—）定义
 # 类变量（class variable—）定义
  #类方法（@classmethod）定义
  #静态方法（@staticmethod）定义
#实例变量-------------------------------------
'''class Dog:
 def __init__(self,k,c,a):
    """asdasdasd"""
    self.kinds=k
    self.color=c
    self.age=a
d1=Dog('京巴','白色',1)
d2=Dog('金毛','黄色',2)
print(d2.kinds,d1.color,d1.age)
print('----------------------------------------------------------------')
class Student:
 def __init__(self,a,b,c):
    """学生管理"""
    self.name=a
    self.age=b
    self.score=c
d=Student('123',18,100)
s1=Student(input('name'),input('age'),input('score'))
print(s1.name)
print(d.__dict__)
print(d.__doc__)'''

'''
构造方法：创建对象时初始化实例变量
def __init__(self[,形参列表]):
   语句
   
析构方法：
class 类名
 __del__(self):
 pass
 
'''
'''
class Human:
    def __init__(self,a,b):
        self.name=a
        self.age=b

    def setNmae(self):
     """添加和修改姓名"""





    def setAge(self):
            """..."""

    def infos(self):
            """显示信息"""
            print("显示信息:",self.name)
            print(self.age)


s1=Human('lv',18)
s2=Human('li',16)
print(s1.name)
print(s1.infos())#用对象来调用
print(s1.setAge())
print(Human.infos(s1))#对类来调用
'''
print('------------------------------------------------------------------------')
'''class Car:
    def __init__(self,a,m,c):
        self.brand=a
        self.moder=m
        self.color=c
    def run(self,speed):
        '多少公里的速度行驶'
        print('正在以',speed,'公里每小时行驶')

    def infos(self):
        '显示颜色'
        return self.color
    def change_color(self):
        "改变颜色"
        return self.color

a4=Car('奥迪','红色','A4')
print(Car.change_color('红色'))
'''


