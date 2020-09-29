class Dog(object):
    def eat(self,food):
        print("小狗正在吃%s"%str(food))
    def sleep(self,time):
        print("小狗睡了%s小时"%str(time))
d = Dog()
# d.eat("骨头")
# d.sleep(1)

#类调用实例方法
Dog.eat(d,"火腿")