l = [int(i) for i in input("Enter list : ").split()]
min_element = l[0]
for i in range(1,len(l)):
    if l[i]<=min_element:
        min_element = l[i]
print(min_element)
