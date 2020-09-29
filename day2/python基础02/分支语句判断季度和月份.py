season = input("请输入您要查找的季度：")
if season == "春天":
    print("春天包含1月2月3月")
elif season == "夏天":
    print("夏天包含4月5月6月")
elif season == "秋天":
    print("秋天包含7月8月9月")
else:
    print("冬天包含10月11月12月")

while 1:
    month = input("请输入您要查找的月份：")
    if month in ("1月","2月","3月"):
        print("这个月属于春天！")
    elif month in ("4月","5月","6月"):
        print("这个月属于夏天！")
    elif month in ("7月","8月","9月"):
        print("这个月属于秋天！")
    elif month in ("10月","11月","12月"):
        print("这个月属于冬天！")
    elif month in ("88","q","exit"):
        break
    else:
        print("您的输入不合法！")
