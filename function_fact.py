def fact(num):
    f=1
    for i in range (2,num+1):
        f=f*i
        return f 
    #print("factorialof {} is:{}".format(num,f))  
   

n=int(input("Enter the number"))
result=fact(n)
print("factorial of is:{}".format(result))
