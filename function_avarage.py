def avg(L):
    sum=0
    for i in L:
        sum=sum+i
    return(sum/len(L))
L=[]
avarage=0
n=int(input("Emter number of elements:"))
for i in range(0,n):
    x=int(input("Enter the elements:"))
    L.append(x)
avarage=avg(L)
print("avarage is:",avarage)

        
