while 1:
    height = input("请输入您的身高(米)：")
    if height == "":
        break
    height = float(height)

    weight = float(input("请输入您的体重(千克)："))
    bmi = weight / height**2
    # print(bmi)

    if bmi < 18.5:
        print("体重过轻")
    elif bmi <24:
        print("正常")
    elif bmi <28:
        print("超重")
    elif bmi <30:
        print("I级肥胖")
    elif bmi <40:
        print("II级肥胖")
    else:
        print("III级肥胖")