list3 = [i * j for i in range(10) for j in range(1,i+1)]
print(list3)

# list1 = ["张飞","关云长","刘备"]
# list2 = ["西门庆","孙悟空","林黛玉","小乔"]
# list3 = [i + j for i in list1 for j in list2]
# print(list3)
# print(len(list3))

#根据花色列表与数字列表，创建扑克牌列表(除了大小王)
list_suit = ["红桃","方片","黑桃","梅花"]
list_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
list_poker = [i + j for i in list_suit for j in list_number]
print(list_poker)
print(len(list_poker))