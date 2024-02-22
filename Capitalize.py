str=input("Enter your string : ")
listword = str.split()
str2 = ' '
for word in listword:
    str2 = str2 + word.capitalize() + ' '

print(str2)