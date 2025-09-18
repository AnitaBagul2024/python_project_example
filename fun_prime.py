
def primenum(x):
    print("in fun",__name__)
    for div in range(2,x):
        if(x%div==0):
            return False
        
   # return True
        
print(__name__)            
x=int(input("Enter the number"))
num1=primenum(x)
if (num1==False):
    print("{} is  not prime number".format(x))
else:
    print("{} is  prime number".format(x))

