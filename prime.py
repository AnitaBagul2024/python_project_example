x=int(input("Enter the range"))
print("prime numbers between 2 to {} are:".format(x))
for num in range(2,x):
    flag=0
    for div in range(2,num):
        if(num%div==0):
            flag=1
            break
    if flag==0:
        print(num,end=" ")
