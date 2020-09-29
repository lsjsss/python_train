number_one = float(input("请输入第一个数字："))
operator = input("请输入运算符：")
number_two = float(input("请输入第二个数字："))
if operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "/":
    print(number_one / number_two)
else:
    print("您的运算符输入有误")