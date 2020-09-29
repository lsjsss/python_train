def get_fibonacci_sequence(length):
    sequence = [1,1]
    for i in range(length - 2):
        sequence.append(sequence[-2] + sequence[-1])
    return sequence

print(get_fibonacci_sequence(10))

# def is_exist_for_double_list(list_target,element):
#     for line in list_target:
#         if element in line:
#             return True
#     return False
#
# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]
# print(is_exist_for_double_list(list01,10))
# print(is_exist_for_double_list(list01,109))

# 变量的作用域
# def func01():
#     a = 10
#     print(a)
# func01()
# 内部变量
# def func02(p1,p2):
#     p1 = 200
#     p2[0] = 200
#
# a = 100
# b = [100]
# func02(a,b)
# print(a)
# print(b)
#对上一题的示例
# def func03(p1,p2):
#     p1 = "A"
#     p2[0] = "B"
# a = ["a"]
# b = ["b"]
# func03(a,b)
# print(a)
# print(b)

# def func04(p1,p2):
#     p1[0] = "孙悟空"
#     p2[0] = "猪八戒"
# a = ["悟空"]
# b = ["八戒"]
# func04(a,b[:])
# print(a)
# print(b)

#全局变量:在文件中定义的变量
# g01 = 100
# def func01():
#     a = 10
# def func02():
#     #在局部作用域中，可以读取全局变量
#     print(g01)
#
# def func03():
#     #声明全局变量
#     global g01
#     g01 = 200
# func03()
# print(g01)
#
# def func04():
#     global g02
#     g02 = 300
# func04()
# print(g02)

#nonlocal 的使用方法
def make_counter():
    count = 0
    def counter():
        nonlocal count#这个不写试试
        count += 1
        return count
    return counter

def test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())
test()