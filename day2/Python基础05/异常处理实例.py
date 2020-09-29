# age = input("请输入您的年龄：")
# try:
#     age = int(age)
#     print("成年" if age >=18 else "未成年")
# except:
#     print("无效的年龄格式")

# age = input("请输入您的年龄：")
# num_a = input("请输入被除数：")
# num_b = input("请输入除数：")
# try:
#     age = int(age)
#     print("成年" if age >=18 else "未成年")
#     print("{}/{}={}".format(num_a,num_b,int(num_a)/int(num_b)))
# except ValueError as ex:
#     print("无效的年龄格式")
#     print(ex)
# except ZeroDivisionError as ex:
#     print(ex)

#异常处理综合实例
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


