#try,except,finaly
n=int(input("Enter your numerator:"))
d=int(input("Enter your denomeniator:"))

try:
    result=n/d
    print(result)
    
except:
     print("Denominator cannot be zero,try again")

finally:print("Program ends")

      
        
