#Python program to find the most occurring character and its count

cnt=0
U_str=input("Enter Your string:")

input_char=input("Enter your char:")

for i in U_str:
    if i==input_char:
        cnt=cnt+1


print("Total number of given char",input_char," count is:",cnt)
