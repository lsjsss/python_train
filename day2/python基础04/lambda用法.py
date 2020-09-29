# func= lambda a,b :a+b
# print(func(12,3))

# func01 = lambda *args:sum(args)
# print(func01(1,3,5,7))
# print(func01(1,3,56,5))

func02 = lambda a = 23,b = 4:a-b
print(func02())
print(func02(b = 10))

func03 = lambda **kwargs:(kwargs.keys(),kwargs.values())
print(func03(a= "apple",b = "banana"))