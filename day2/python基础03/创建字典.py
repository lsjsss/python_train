dict1 = {"name":"zou","age":18,"height":180}
dict2 = dict([(101,"悟空"),(102,"悟净"),(103,"悟能")])
print(type(dict1))
print(dict1)
print(type(dict2))
print(dict2)
dict2[104] = "唐僧"
print(dict2)
dict2[102] = "潘金莲"
print(dict2)
del dict1["name"]
print(dict1)
# 循环遍历字典
for key in dict1:
    print(key)
    print(dict1[key])

for key,value in dict1.items():
    print(key)
    print(value)

for value in dict1.values():
    print(value)