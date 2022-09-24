#列表 ，元组。字典，集合
'''L=[1,2,3,[3.1,3.2]]
print(type(L))
b=list('hello')
print(b[0])
x=[1,2,3]
y=[4,5,6]
z=x+y
print(z)'''
#作比较时，对应上的类型要一致
#列表切片就是替换，步长为1随便换，步长不是1要注意个数问题
'''x[0:1]=[200,300,400]
print(x)
a=input('输入第一个数')
b=input('输入第二个数')
c=input('输入第三个数')
d=[a,b,c]
print('最大值为',max(d),'最小值为',min(d))
'''
'''a=[1,5,6,89,9]
a.sort()
a.reverse()
print(a)
a.pop()
print(a)'''
'''import copy
l=[20,21,22]
l1=[10,l,30]
l2=copy.deepcopy(l1)
l[2]=25
print(l1)
print(l2)'''
#列表是可迭代对象
'''''
l=[1,2,3,4]
for x in l :
    print(x*x)
#列表推导式：列表推导式是用可迭代对象，依次生成列表内元素的方式，语法：【表达式 for 变量 in 可迭代对象】
#或【后面加一个if
l1=[i**2 for i in l]
print(l1)
#元组就是一个不能改变的列表
x,y=[100,200]
print(x)
print(y)
l=input('输入一个数字')
'''
#字典{’键’：值，。。。。。}字典的键是不能改变类型，比如元组，bool 不能充当key的是list，dict和set
#字典的遍历
'''d={'age':30,'score':20}
for k,v in d.items():
    print(k,':',v)
#集合，没有value的字典'''


