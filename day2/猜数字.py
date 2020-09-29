import random
random_number = random.randint(1, 100)

count = 0
while 1:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("您猜的数字大了")
    elif input_number < random_number:
        print("您猜的数字小了")
    else:
        print("恭喜您猜对了，大吉大利，总共猜了", count, "次")
        break