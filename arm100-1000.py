print("all three digit armstrong numbers are:")
for x in range(100,1000):
    sum=0
    arm=x
    while(x!=0):
        unit=x%10
        sum=sum+unit**3
        x=x//10
    if(sum==arm):
        print(arm)
    
