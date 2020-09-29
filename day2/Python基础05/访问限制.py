#属性访问限制
# class Turtle:
#     def __init__(self):
#         self._name = "小甲鱼"#保护属性
# t = Turtle()
# print(t._name)
# 私有属性正常访问不了
# class Turtle:
#     def __init__(self):
#         self.__name = "小甲鱼"#私有属性
# t = Turtle()
# print(t.__name)
# python 当中私有属性是伪私有
# class Turtle:
#     def __init__(self):
#         self.__name = "小甲鱼"#私有属性
# t = Turtle()
# print(t._Turtle__name)
#  1   定义方法访问私有属性
# class Turtle:
#     def __init__(self):
#         self.__name = "小甲鱼"#私有属性
#     def get_name(self):
#         return self.__name
#     # def set_name(self,name):
#     #     self.__name = name
# t = Turtle()
# # t.set_name("小美鱼")
# print(t.get_name())

# 2  通过装饰器访问私有属性
# class Turtle:
#     def __init__(self):
#         self.__name = "小甲鱼"#私有属性
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name = name
# t = Turtle()
# t.name = "小花鱼"
# print(t.name)


