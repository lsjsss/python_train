#  类方法里面的类方法
class Turtle:
    age = 100
    @classmethod
    def get_age(cls):
        return cls.age

    @classmethod
    def set_age(cls,age):
        cls.age = age

print(Turtle.get_age())
Turtle.set_age(1000)
print(Turtle.get_age())

#静态方法
# class Turtle:
#
#     @staticmethod
#     def s_fun(name,age):
#         return name,age
# print(Turtle.s_fun("美人鱼",500))