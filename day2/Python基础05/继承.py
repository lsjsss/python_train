# Pet 宠物类
class Pet(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("my name is {},i am {} years old".format(self.name,self.age))

# p1 = Pet("明明",7)
# p1.info()

class Cat(Pet):
    def __init__(self,name,age):
        super(Cat,self).__init__(name,age)

class Dog(Pet):
    def __init__(self,name,age):
        super(Dog,self).__init__(name,age)

cat1 = Cat("TOM",4)
dog1 = Dog("kitty",2)
print(cat1.info())
print(dog1.info())
