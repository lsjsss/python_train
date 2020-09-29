#将厚度换算成米
thickness = 0.01/1000
count = 0

while thickness <= 8844.43:
    thickness *= 2
    count += 1
    print("第",count,"次对折的厚度是",thickness)
print(count)