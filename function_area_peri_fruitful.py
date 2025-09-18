import math
def area_peri(r):
    A=math.pi*r**2
    P=2*math.pi*r
    print(type(A))
    return(A,P)
radius=float(input("Enter the radius:"))
(a,p)=area_peri(radius)

print("Area of circle is: {:.2f} and Perimeter of circle is: {}".format(a,p))
    
    
