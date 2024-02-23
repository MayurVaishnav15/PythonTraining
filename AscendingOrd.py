l = [int(i) for i in input("Enter list : ").split()]
for i in range (len(l)):
    for j in range(i+1,len(l)):
        if l[i]>=l[j]:
            temp = l[i]
            l[i]= l[j]
            l[j]=temp
print("sorted List",l)
print("Descending List",l[::-1])


    
