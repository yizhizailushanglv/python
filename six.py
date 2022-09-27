#运算符重载
'''''

class MyNamber:
    "此类用于定义一个整形数字类，用于演示Str重载"
    def __init__(self,value):
        self.data=value
    def __repr__(self):
        print('__repr__被调用')
        return "Mynamber("+repr(self.data)+")"
    def __str__(self):
        print("__str__被调用")
        return "整形数值("+str(self.data)+")"
n1=MyNamber(100)
n2=MyNamber(200)
print(repr(n1))
print(str(n2))
print(n1)
print(n2)
'''

