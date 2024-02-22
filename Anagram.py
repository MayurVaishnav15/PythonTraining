str1 = input("Enter string 1")
str2 = input("Enter string 2")

str3=sorted(str1)
str4=sorted(str2)
if str3==str4:
    print("Anagram")
else:
    print("Not")
