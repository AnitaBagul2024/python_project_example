L=[]
n=int(input("Enter number of students:"))
sum=0
for i in range(0,n):
    L1=[]
    x=int(input("Enetr roll no:"))
    L1.append(x)
    y=input("Enetr name:")
    L1.append(y)
    M=[]
    for m in range(0,5):
        z=float(input("Enetr marks:"))
        M.append(z)
        sum=sum+z
    avg=sum/5
    L1.append(M)
    L1.append(avg)
    L.append(L1)
print(L)
print("Roll No.\tName\t\t\tMarks\t\t\tAverage")
for j in range(0,n):
    print()
    for k in range(0,4):
        print(L[j][k],end='\t\t')
    
