#简单的测试
import json
def show_categories(*cnames):
    print("所有类别的名称如下：")
    for name in cnames:
        print(name,end=" ")

show_categories("饮料","水果","蔬菜")
#读取json文件
import json
def show_categories(*cnames):
    print("所有类别的名称如下：")
    for name in cnames:
        print(name,end=" ")
with open("northwind.json","rb") as f:
    data = json.loads(f.read())
    # print(data)
categories = tuple({p["CategoryName"] for p in data})
show_categories(*categories)

#字典传参
# import json
#
# with open("northwind.json","rb") as f:
#     data = json.loads(f.read())
#
# def show_info(**kwargs):
#     for k,v in kwargs.items():
#         print("{}:{}".format(k,v))
# while 1:
#     num = int(input("请输入产品编号(1-79):"))
#     show_info(**data[num-1])
