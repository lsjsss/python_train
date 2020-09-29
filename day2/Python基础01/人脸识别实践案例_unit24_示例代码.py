# # 函数的创建和调用
# def attack01():
#     '''
#     第一种攻击方式
#     :return:
#     '''
#     print("直拳")
#     print("摆拳")
#     print("勾拳")
#     print("肘击")
# # attack01()
# #
# def attack02(count):
#     '''
#     急眼了，胡打一通
#     :param count:
#     :return:
#     '''
#     for _ in  range(count):
#         attack01()
#         print()
#
# attack02(3)
#
# # 定义函数求斐波拉契数列
# def get_fibonacci_sequence(count):
#     sequence = [1,1]
#     for i in range(count-2):
#         sequence.append(sequence[-1]+sequence[-2])
#     return sequence
#
# fib = get_fibonacci_sequence(10)
# print(fib)
#
# # 函数传参
# 位置传参
# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# func(1,2,3)
# # 缺省参数
# def func(a=1,b=9,c=9):
#     print(a)
#     print(b)
#     print(c)
# func(2,3)
# 序列传参
# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# list01 = ["A","B","C"]
# list01 = ("A","B","C")
# set01 = {"A","B","C"}
# func(*set01)
#
# # 关键字传参
# func(a= 12,c = 17,b=19)
# #字典传参
# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# dict01 = {"a":"a1","b":"b1","c":"c1"}
# func(**dict01)
#
# # zip函数
# a,b,c = zip(["a","b","c"],[1,2,3])
# a,b,c = zip(("a","b","c"),[1,2,3])
# a,b,c = zip(("a","b","c"),[1,2,3,4])
# a,b,c,d = zip(("a","b","c","d"),[1,2,3,4])
# a,b,c,d = zip("CHINA",[1,2,3,4])
# print(a)
# print(b)
# print(c)
# print(d)
#
# # with 语句创建文件并且写入文件
# with open("zwq.txt","a",encoding="utf-8") as f:
#     f.write("world")

# # 写入json文件
# import json
# a = {"name":"zouwuqi","age":20,"weight":150,"height":180}
# with open("zwq.json","w",encoding="utf-8") as f:
#     f.write(json.dumps(a,indent=2,sort_keys=False))
#
# # 读取json文件
# import json
# with open("zwq.json","r",encoding="utf-8") as f:
#     data1 = json.loads(f.read())
#     f.seek(0)
#     data2 = json.load(f)
# print(data1)
# print(data2)
#
#异常处理综合实例
# age = input("请输入您的年龄：")
# numa = input("请输入被除数：")
# numb = input("请输入除数：")
# try:
#     age = int(age)
#     if age <0 or age>=200:
#         raise Exception("年龄范围不正确！")
#     print("成年" if age >= 18 else "未成年")
#     print('{}/{}={}'.format(numa,numb,int(numa)/int(numb)))
# except ValueError as ex:
#     print("无效的年龄格式")
#     print(ex)
# except ZeroDivisionError as ex:
#     print(ex)
# except Exception as ex:
#     print(ex)
# else:
#     print("程序成功执行完毕！！")
# finally:
#     print("程序结束~")
#
# # 定义类的属性
# class Turtle:
#     color = "绿色"
#     weight = 10
#     legs = 4
#     shell = True
#
# t1 = Turtle()
# print(t1.color)
# print(t1.weight)
# print(t1.legs)
# print(t1.shell)

# #定义类的方法
# class Turtle:
#     def climb(self):
#         print("小乌龟很努力的向前爬")
#     def run(self):
#         print("小乌龟很努力的向前逃窜")
# t2 = Turtle()
# t2.climb()
#
# #通过实例调用方法
# class Dog(object):
#
#     def eat(self,food):
#         print("小狗正在吃"+str(food))
#
#     def sleep(self,time):
#         print("小狗睡了"+str(time)+"小时")
# d = Dog()
# d.eat("骨头")
# d.sleep(2)
# Dog.eat(d,"狗粮")
#
# class Teacher(object):
#     def teaching(self,skill):
#         print("teaching "+str(skill))
#
# class student(object):
#     def learning(self,skill):
#         print("learning "+str(skill))
#
# t1 = Teacher()
# t1.teaching("python")
# s1 = student()
# s1.learning("java")
#
# #创建类的构造方法
# class Turtle:
#     def __init__(self,name):
#         self.name = name
#     def climb(self):
#         print("我叫%s，正在很努力向前爬！"%(self.name))
#
# t3 = Turtle("绿饼干")
# t3.climb()
# t4 = Turtle("土豆")
# t4.climb()
#
# #初始化实例
class Car(object):
    def __init__(self,color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model

    def run(self,speed):
        print("一辆",self.color,self.brand,self.model,"以每小时",speed,"公里在道路上狂奔")

c1 = Car("红色","奥迪","A4")
print(c1.__dict__)
c2 = Car("蓝色","比亚迪","E5")
print(c2.__dict__)
c1.run(200)
c2.run(100)
