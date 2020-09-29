set1 = set()
set1 = set(range(1,11))
print(set1)
set2 = {}
print(type(set1))
print(type(set2))
list1 = [11,12,2,3,4,2,3,5,6,3,4,6]
set1 = set(list1)
list2 = list(set1)
print(set1)
set1.add(7)
print(set1)
set1.discard(11)
print(set1)

