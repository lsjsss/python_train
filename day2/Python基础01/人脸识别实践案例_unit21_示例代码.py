# pycharm 快捷键测试，程序运行测试
print("hello world my name is xxx")
print("hello world my name is xxx")
print("hello world ")
print("hello world my name is xxx")
print("hello world my name is xxx")
print("hello world my name is xxx")
print("hello")

#变量的一些操作
a = 100
_a = 200
print(a)
print(_a)
name = "大名"
print(name)

num01 = 1000
num02 = num01
print(num01)
print(num02)
print(id(num01))
print(id(num02))

num01 = num02 = num03 =  2000
print(num01)
print(num02)
print(num03)

num01,num02,num03,num04 = 1000,2000,3000,4000
print(num01)
print(num02)
print(num03)
print(num04)

# 变量直接交换
num01,num02= 1000,2000
num01,num02 = num02,num01
print(num01)
print(num02)
# #需要第三方的变量交换
num01,num02 = 100,200
num03 = num01
num01 = num02
num02 = num03
print(num01)
print(num02)

# #不同数据类型之间的转换
num01 = 2.8
num02 = 8
num03 = str(2+6)
num04 = bool(0.0)
# print(int(num01))
# print(float(num02))
print(num03)
print(type(num03))
print(num04)