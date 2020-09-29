# RMB = int(input("你给女朋友花了多少钱："))
# if 0<= RMB < 200:
#     print("你不够重视我")
# elif 200<= RMB <=1000:
#     print("你够重视我")
# else:
#     print("你太重视我了")

# if 1:
#     print("真值")
RMB = int(input("过节你给女朋友花了多少钱："))
if 0<= RMB < 200:
    print("你不够重视我")
else:
    print("你重视我")

RMB = int(input("过节你给女朋友花了多少钱："))
num = "你不够重视我" if 0<= RMB < 200 else "你重视我"
print(num)