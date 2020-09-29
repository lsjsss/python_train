score01 = float(input("请输入第一个同学的成绩："))
score02 = float(input("请输入第二个同学的成绩："))
score03 = float(input("请输入第三个同学的成绩："))
score04 = float(input("请输入第四个同学的成绩："))

#假设最大值
max_score = score01
if max_score < score02:
    max_score = score02
if max_score < score03:
    max_score = score03
if max_score < score04:
    max_score = score04

print("最高分是：",max_score)
#拓展知识点
L = [score01,score02,score03,score04]
# print("最高分是第",L.index(max_score)+1,"位同学","最高分是：",max_score)
print("最高分是第",L.index(max(L))+1,"位同学","最高分是：",max(L))