L=[]
n=int(input("Enter number of students:"))
for i in range(0,n):
    L1=[]
    x=int(input("Enetr roll no:"))
    L1.append(x)
    y=input("Enetr name:")
    L1.append(y)
    z=float(input("Enetr marks:"))
    L1.append(z)
    L.append(L1)
print("Roll No.\tName\t\t\tMarks")
for i in range(0,n):
    print()
    for j in range(0,3):
        print(L[i][j],end='\t\t')
    
