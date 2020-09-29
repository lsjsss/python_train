#map函数的使用方法
# a = map(str,[1,2,3,4,5])
# print(list(a))
# #
# b = map(str,[1,2,3])
# print(list(b))
#
# c = map(ord,"中国两会")
# print(list(c))

# d = map(chr,[10675,34567,28736])
# print(list(d))

# for i in [10675,34567,28736]:
#     print(chr(i),end=' ')

# filter
def is_odd(n):
    return n%2==1
print(is_odd(20))
a = filter(is_odd,range(100))
print(tuple(a))

# def is_leap_year(n):
#     return n%4==0 and n%100!=0 or n%400==0
# b = filter(is_leap_year,range(1970,2200))
# print(list(b))

# zip函数
# a,b,c = zip(["a","b","c"],[1,2,3])
# a,b,c = zip(("a","b","c"),[1,2,3])
# a,b,c = zip(("a","b","c"),[1,2,3,4])
# a,b,c,d = zip(("a","b","c","d"),[1,2,3,4])
a,b,c,d = zip("CHINA",[1,2,3,4])
print(a)
print(b)
print(c)
print(d)
#reduce 高阶函数
# from functools import reduce
# def add(x,y):
#     return x+y
# a = reduce(add,(1,2,3,4,5))
# print(a)

#sorted函数
# list01 = [2,3,5,1,-67,-23,89,34,62]
# print(sorted(list01,key=abs))