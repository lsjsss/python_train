#调用实例方法
class Dog(object):

    def eat(self,food):
        print("小狗正在吃"+str(food))

    def sleep(self,time):
        print("小狗睡了"+str(time)+"小时")
d = Dog()
d.eat("骨头")
d.sleep(2)

# Dog.eat(d,"狗粮")
#
class Teacher(object):
    def teaching(self,skill):
        print("teaching "+str(skill))

class student(object):
    def learning(self,skill):
        print("learning "+str(skill))

t1 = Teacher()
t1.teaching("python")
s1 = student()
s1.learning("java")

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

#异常处理
age = input("请输入您的年龄：")
if age.isdigit():
    age = int(age)
    print("成年" if age >= 18 else "未成年")
else:
    print("无效的年龄格式")

age = input("请输入您的年龄：")
try:
    age = int(age)
    print("成年" if age >= 18 else "未成年")
except:
    print("无效的年龄格式")
#异常
age = input("请输入您的年龄：")
numa = input("请输入被除数：")
numb = input("请输入除数：")
try:
    age = int(age)
    if age <0 or age>=200:
        raise Exception("年龄范围不正确！")
    print("成年" if age >= 18 else "未成年")
    print('{}/{}={}'.format(numa,numb,int(numa)/int(numb)))
except ValueError as ex:
    print("无效的年龄格式")
    print(ex)
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("程序成功执行完毕！！")
finally:
    print("程序结束~")