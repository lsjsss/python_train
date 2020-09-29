Price = int(input("请输入物品单价："))
Count = int(input("请输入物品数量："))
Total_money = Price * Count
print("总价格：", Total_money)
Actually_money = int(input("用户实际付款："))
back_money = Actually_money - Total_money
print("应找回：", back_money)





