price = int(input("请输入商品的单价:"))
count = int(input("请输入商品的数量:"))
total_money = int(input("顾客总共给的钱数："))
back_money = total_money - price*count
print("应找回：",back_money,"元")