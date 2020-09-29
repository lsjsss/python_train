#第一题
# list1_planets = ["水星","金星","水星","地球"]
# # list2_planets= list1_planets.extend(["火星","木星","土星","天王星","海王星"])
# # print(list2_planets)
# list2_planets = ["水星","金星","水星","地球","火星","木星","土星","天王星","海王星"]
# print(list2_planets[0])
# print(list2_planets[-1])
# print(list2_planets[:3])
# print(list2_planets[4:])
# list2_planets.remove("天王星")
# print(list2_planets)
# list3_planets = list2_planets[::-1]
# print(list3_planets)
# for i in list3_planets:
#     print(i)

#第二题
# list_score = []
# while 1:
#     score = input("请输入学生成绩：")
#     if score == "":
#         break
#     list_score.append(int(score))
# print(list_score)
# print(max(list_score))
# print(min(list_score))
# print(sum(list_score)/len(list_score))

#找出1970年到2050年之间所有的闰年，存入列表当中
# list1 = []
# for year in range(1970,2051):
#     if year % 4==0 and year%100 != 0 or year % 400 == 0:
#         list1.append(year)
# print(list1)

#用列表推导式
# list1 = [year for year in range(1970,2051)\
#          if year % 4 ==0 and year % 100!=0 or year % 400 == 0]
# print(list1)

"""彩票模拟器
双色球
红色：6个  1--33之间的整数
不能重复
蓝色：1个  1--16之间的整数
-- 随机产生一注彩票(列表,前六个元素表示红球,最后一个元素表示蓝球)random（猜数字）
-- 在终端中录入一注彩票       提示：号码超过范围、号码已经存在"""

import random
#用列表接收随机产生的一注彩票  先确定前六个红球
list_ticket = []
while len(list_ticket) < 6:
    number = random.randint(1,33)
    # print(number)
    if number not in list_ticket:
        list_ticket.append(number)
print(list_ticket)
# #确定最后一个篮球
list_ticket.append(random.randint(1,16))
print(list_ticket)

list_ticket = []
while len(list_ticket) < 6:
    number = int(input("请输入第%d个红球号码(1-33):"%(len(list_ticket)+1)))
    if number < 1 or number >33:
        print("号码超过范围")
    elif number in list_ticket:
        print("号码已经存在")
    else:
        list_ticket.append(number)
#确定最后一个篮球
while len(list_ticket) < 7:
    number = int(input("请输入篮球的号码(1-16)："))
    if number < 1 or number > 16:
        print("号码超过范围")
    else:
        list_ticket.append(number)
print(list_ticket)