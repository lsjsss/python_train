def is_exist_for_double_list(list_target,element):
    for line in list_target:
        if element in line:
            return True
    return False

list_erwei = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
while 1:
    element = int(input("请输入要判断的元素："))
    print(is_exist_for_double_list(list_erwei,element))

