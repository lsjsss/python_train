class Turtle:
    def __init__(self,name):
        self.name = name
    def climb(self):
        print("我叫%s，正在很努力向前爬！"%(self.name))

t3 = Turtle("绿饼干")
t3.climb()
t4 = Turtle("土豆")
t4.climb()
