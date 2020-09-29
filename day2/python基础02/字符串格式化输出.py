name  = input("请输入您的名字：")
age  =  input("请输入您的年龄：")
print("我的名字是",name,"我的年龄是",age)
print("我的名字是%s，我的年龄是%s"%(name,age))

# 练习
jin = 5
liang = 8
print("%d斤零%d两"%(jin,liang))
# 5+6=11
num01 = 5
num02 = 6
print("%d+%d=%d"%(num01,num02,num01+num02))

name = "灭霸"
alt = 999
hp = 1000.0
print("%.2s的攻击力是%d,血量是%.2f"%(name,alt,hp))
print("{}的攻击力是{},血量是{}".format(name,alt,hp))