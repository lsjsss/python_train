# chr ord 函数操作方法
message = "我是春光灿烂猪八戒"
for i in message:
    print(i, "的unicode码是", ord(i))
print(max(message))
print(min(message))
for j in range(10000, 11100):
    print(j, ":", chr(j))

str_input = input("请输入一段字符串：")
for i in str_input:
    print(i, ord(i))

while 1:
    str_input = int(input("请输入unicode码："))
    if str_input == "":
        break
    print(chr(str_input))

# index 索引
message = "我是春光灿烂猪八戒"
print(message[2])
print(message[-7])
print(message[-99])
print(message[89])
print(len(message))

message = "我是春光灿烂猪八戒"
print(message[2:6])
print(message[6:])
print(message[:])
print(message[::2])
print(message[::])
print(message[1:-3:1])
print(message[-4:1:-1])
print(max(message))

#字符串的格式化输出
name  = input("请输入您的名字：")
age  =  input("请输入您的年龄：")
# print("我的名字是"+name,"我的年龄是"+age)
print("我的名字是%s，我的年龄是%s"%(name,age))

# 练习
jin = 5
liang = 8
print("%d斤零%d两"%(jin,liang))
# 5+6=11
num01 = int(input("请输入第一个数："))
num02 = int(input("请输入第二个数："))
print("%d+%d=%d"%(num01,num02,num01+num02))

name = "灭霸"
alt = 999
hp = 1000.0
# print("%s的攻击力是%d,血量是%.2f"%(name,alt,hp))
print("{}的攻击力是{},血量是{}".format(name,alt,hp))

# 列表
list1 = ["孙悟空",100,True,[2,3,4]]
print(list1)
list2 = list("wo shi zhong guo ren ")
print(list2)
#列表操作
list1 = []
for i in "wo shi zhong guo ren ":
    list1.append(i)
print(list1)
list1.append("we")
print(list1)
list1 = ["宋江","武松","吴用","孙悟空"]
list1.insert(3,"猪八戒")
print(list1)
list1[1] = "武大郎"
print(list1)
name1 = list1[0]
print(name1)
list1 = ["宋江","武松","吴用","孙悟空"]
print(list1[:-2])
print(list1[:2])

list1[-2::-1] = [False,"唐三藏",True]
print(list1)
list1.remove("唐三藏")
list1.remove(list1[1])
print(list1)
del list1[1:2]
print(list1)
list2 = list1[:3]
print(list2)

#列表推导式
list2 = [i**2 for i in list1 if i%2]
print(list2)
list2 = [i**2 for i in list1]
print(list2)

#根据花色列表与数字列表，创建扑克牌列表(除了大小王)
list_suit = ["红桃","方片","黑桃","梅花"]
list_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
list_poker = [i + j for i in list_suit for j in list_number]
print(list_poker)
print(len(list_poker))

#元组
names = ("孙悟空","猪八戒","沙悟净","唐三藏")
dashixiong = names[0]
print(dashixiong)
ershazi = names[1:3]
print(ershazi)

for name in names:
    print(name,end=" ")

tuple1 = (34,23,45,6,8,9)
list1  = list(tuple1)
list1.append(1000)
list1.insert(2,1111)
tuple1 = tuple(list1)
print(tuple1)

#字典
dict1 = {"name":"zou","age":18,"height":180}
dict2 = dict([(101,"悟空"),(102,"悟净"),(103,"悟能")])
print(type(dict1))
print(dict1)
print(type(dict2))
print(dict2)
dict2[104] = "唐僧"
print(dict2)
dict2[102] = "潘金莲"
print(dict2)
del dict1["name"]
print(dict1)
# 循环遍历字典
for key in dict1:
    print(key)
    print(dict1[key])

for key,value in dict1.items():
    print(key)
    print(value)

for value in dict1.values():
    print(value)

#字典推导式
dict2 = dict([(101,"悟空"),(102,"悟净"),(103,"悟能"),(104,"唐僧")])
print(dict2)
dict3 = {key:value for key,value in dict2.items()}
print(dict3)

#集合
# set1 = set()
set1 = set(range(1,11))
print(set1)
set2 = {}
print(type(set1))
print(type(set2))
list1 = [11,12,2,3,4,2,3,5,6,3,4,6]
set1 = set(list1)
list2 = list(set1)
print(set1)
set1.add(7)
print(set1)
set1.discard(11)
print(set1)

#集合的运算
s1 = {2,3,4}
s2 = {2,3,44}
s3 = s1 & s2
print(s3)

s1 = {2,3,4}
s2 = {2,3,44}
s4 = s1 | s2
print(s4)

s5 = s1-s2
s6 = s2-s1
print(s5)
print(s6)

s7 = s1 ^ s2
print(s7)

#集合推导式
set1 = {i for i in range(10) if i % 2==1}
print(set1)

