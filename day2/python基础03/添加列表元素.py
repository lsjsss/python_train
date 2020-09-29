list1 = []
for i in "wo shi zhong guo ren ":
    list1.append(i)
print(list1)
list1.append("we")
print(list1)
list1 = ["宋江","武松","吴用","孙悟空"]
list1.insert(3,"猪八戒")
print(list1)
list1[1] = "武大郎"
print(list1)
name1 = list1[0]
print(name1)
list1 = ["宋江","武松","吴用","孙悟空"]
# print(list1[:-2])
# print(list1[:2])

list1[-2::-1] = [False,"唐三藏",True]
print(list1)
# list1.remove("唐三藏")
list1.remove(list1[1])
print(list1)
del list1[1:2]
print(list1)
list2 = list1[:3]
print(list2)