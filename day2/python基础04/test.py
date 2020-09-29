# def attack01():
#     """
#     第一种攻击方式
#     """
#     print("直拳")
#     print("摆拳")
#     print("勾拳")
#     print("肘击")
#
# def attack02(count):
#     """
#     第二种攻击方式
#     :param count: int类型，次数
#     :return:
#     """
#     for _ in range(count):
#         attack01()
# # attack02(3)
# # attack02(5)
# attack01()

# def add():
#     number01 = float(input("请输入第1个数字："))
#     number02 = float(input("请输入第2个数字："))
#     result = number01 + number02
#     print("结果是：",result)
# add()

# def add(number01,number02):
#     return number01 + number02
# result = add(5,3)
# print(result)



# def print_double_list(list_target):
#     for line in list_target:
#         for item in line:
#             print(item,end = "\t")
#         print()
#
# #测试
# list01 = [
#     [1,2,3],
#     [4,5,6],
# ]
# print_double_list(list01)
#
# list02 = [
#     [5,2,3],
#     [4,54,6],
# ]
# print_double_list(list02)

# def func01(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# # 关键字实参 按照名称将实参传递给形参
# func01(c=3, b=12, a=1)
# # 字典传参：使用双星号修饰，将字典中的元素拆分后与形参按名称（key）对应
# dict01 = {"a":"a1","b":"b2","c":"c3"}
# func01(**dict01)

# #位置传参
# func01(1,2,3)
# #序列传参
# list01 = ["a","b","c"]
# func01(*list01)
# set01 = {"a","b","c"} #不报错，但是无序，所以没有任何意义
# func01(*set01)
