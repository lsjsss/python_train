# 定义类的属性
class Turtle:
    color = "绿色"
    weight = 10
    legs = 4
    shell = True

t1 = Turtle()
print(t1.color)
print(t1.weight)
print(t1.legs)
print(t1.shell)

#定义类的方法
class Turtle:
    def climb(self):
        print("小乌龟很努力的向前爬")
    def run(self):
        print("小乌龟很努力的向前逃窜")
t2 = Turtle()
t2.climb()