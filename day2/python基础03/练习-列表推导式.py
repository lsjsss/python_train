list1 = [34,56,3,5,89,76]
list2 = []
for i in list1:
    j = i+1
    list2.append(j)
print(list2)
list2 = [i + 1 for i in list1]
print(list2)

#奇数
list1 = [34,56,3,5,89,76]
# list2 = []
# for i in list1:
#     if i%2:
#         continue
#     else:
#         list2.append(i)
# print(list2)
#转换成推导式
list2 = [i**2 for i in list1 if i%2]
print(list2)
list2 = [i**2 for i in list1]
print(list2)


