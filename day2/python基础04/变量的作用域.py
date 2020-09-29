g01 = 100

def func01():
    global a
    a = 20
    print(g01)
    print("func01_a>", a)

def func02():
    print(g01)
    print("a",a)
func01()
print(a)
func02()

# def func03():
#     global g01
#     g01 = 200
#
# def func04():
#     global g02
#     g02 = 300
# func04()
# print(g02)

# func03()
# print(g01)
# func02()
# func01()