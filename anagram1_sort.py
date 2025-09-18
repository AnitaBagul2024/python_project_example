str1=input("Enter the first string:")
str2=input("Enter the second string:")
flag=0
for char in str1:
    if char in str2:
        flag=1
        break
if flag==1:
     print("Strings {} and {} are anagrams".format(str1,str2))
else:
    print("Strings {} and {} are  not anagrams".format(str1,str2))
