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
def func(a,b,c):
    print(a)
    print(b)
    print(c)
# list01 = ["A","B","C"]
# func(*list01)
# list01 = ("A","B","C")
# func(*list01)
set01 = {"A","B","C"}
func(*set01)

# 关键字传参
# func(a= 12,c = 17,b=19)
# #字典传参
def func(a,b,c):
    print(a)
    print(b)
    print(c)
dict01 = {"a":"a1","b":"b1","c":"c1"}
func(**dict01)