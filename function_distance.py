import math
def distance(x1,x2,y1,y2):
    d=math.sqrt((y2-y1)**2+(x2-x1)**2)
    return(d)
x1=int(input("Enter the x co-ordinate of first point:"))
y1=int(input("Enter the y co-ordinate of first point:"))
x2=int(input("Enter the x co-ordinate of second point:"))
y2=int(input("Enter the y co-ordinate of second point:"))
d=distance(x1,x2,y1,y2)
print("Distance between two points is:{}".format(d))
