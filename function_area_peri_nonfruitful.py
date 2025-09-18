import math
def area_peri(r):
    A=math.pi*r**2
    P=2*math.pi*r
    print("Area of circle is: {} and Perimeter of circle is {}".format(A,P))

radius=float(input("Enter the radius of circle:"))
area_peri(radius)
