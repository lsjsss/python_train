# # 算术运算符
# a = 3
# b = 7
# print(a + b)
# print(a - b)
# print(a * b)
# print(int((b / a)))
# print(b // a)
# print(b % a)
# print(b ** a)
# # 比较运算符
# a = 19
# b = 12
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)
# # 逻辑运算符
# # and 洁癖 一假俱假
# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)
#
# print(1 and 5)#5
# print(1 and 0)#0
# print(0 and 5)#0
#
# # or 乐观派 一好俱好
# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)
#
# print(1 or 5)
# print(1 or 0)
# print(0 or 5)
# print(0 or 0)
#
# # not 运算 取反
# print(not True)
# print(not False)
#
# # 复杂的短路运算
# print(1 and 8 or True)#8
# print(1 and 8 or False)#8
# print(1 and False or False)#False
#
#收银台————练习
# price = int(input("请输入商品的单价:"))
# count = int(input("请输入商品的数量:"))
# total_money = int(input("顾客总共给的钱数："))
# back_money = total_money - price*count
# print("应找回：",back_money,"元")
#求加速度
# s = int(input("请输入路程的距离："))
# t = int(input("请输入所需的时间："))
# v = int(input("请输入初速度："))
# a = 2*(s-v*t)/t**2
# print("加速度是",a)
# #判断闰年————练习
# year = int(input("请输入一个年份："))
# result = year % 4 == 0 and year % 100 !=0 or year % 400 == 0
# print(result)
#
# #if else 分支结构
# RMB = int(input("过节你给女朋友花了多少钱："))
# if 0<= RMB < 200:
#     print("你不够重视我")
# else:
#     print("你重视我")
#
# RMB = int(input("过节你给女朋友花了多少钱："))
# num = "你不够重视我" if 0<= RMB < 200 else "你重视我"
# print(num)
# # 练习1
# while 1:
#     month = input("请输入您要查找的月份：")
#     if month in ("1月","2月","3月"):
#         print("这个月属于春天！")
#     elif month in ("4月","5月","6月"):
#         print("这个月属于夏天！")
#     elif month in ("7月","8月","9月"):
#         print("这个月属于秋天！")
#     elif month in ("10月","11月","12月"):
#         print("这个月属于冬天！")
#     elif month in ("88","q","exit"):
#         break
#     else:
#         print("您的输入不合法！")
# # 练习2
# score01 = float(input("请输入第一个同学的成绩："))
# score02 = float(input("请输入第二个同学的成绩："))
# score03 = float(input("请输入第三个同学的成绩："))
# score04 = float(input("请输入第四个同学的成绩："))
# #
# # #假设最大值
# max_score = score01
# if max_score < score02:
#     max_score = score02
# if max_score < score03:
#     max_score = score03
# if max_score < score04:
#     max_score = score04
#
# print("最高分是：",max_score)
#
# # 打印乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}\t".format(i,j,i*j),end="")
#     print()
# # range 函数
# for i in range(10):
#     print(i)
# for i in range(10):
#     print(i,end=" ")
# for i in range(1,11,2):
#     print(i,end=" ")
# print("=============")
# for a in range(0,10,2):
#     print(a,end=" ")
#
# # break continue
# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(i,end=" ")
#
# for i in range(1,11):
#     if i % 2 == 0:
#         break
#     print(i,end=" ")
#
# #猜数字游戏
# import random
# random_number = random.randint(1,100)
# count = 0
# while 1:
#     count += 1
#     input_number = int(input("请输入数字："))
#     if input_number > random_number:
#         print("您猜的数字大了")
#     elif input_number < random_number:
#         print("您猜的数字小了")
#     else:
#         print("恭喜您猜对了，大吉大利,总共猜了",count,"次")
#         break
#
# #BIM计算
while 1:
    height = input("请输入您的身高(米)：")
    if height == "":
        break
    height = float(height)

    weight = float(input("请输入您的体重(千克)："))
    bmi = weight / height**2
    # print(bmi)

    if bmi < 18.5:
        print("体重过轻")
    elif bmi <24:
        print("正常")
    elif bmi <28:
        print("超重")
    elif bmi <30:
        print("I级肥胖")
    elif bmi <40:
        print("II级肥胖")
    else:
        print("III级肥胖")