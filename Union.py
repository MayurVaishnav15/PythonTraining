list1 = [int(i) for i in input("Enter list : ").split()]
print(list1)
list2 = [int(i) for i in input("Enter list : ").split()]
print(list2)
list3 = []
for i in list1:
    if i not in list3:
        list3.append(i)

for i in list2:
    if i not in list3:
        list3.append(i)
print("The Union is ",list3)
