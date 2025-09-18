#class and method
# as str method is used no need to call print

import math
class point():
    """x,y"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return("%d,%d"%(self.x,self.y))
##    def print_point(self):
##        print(self.x,self.y)
    def get_point(self):
        self.x=int(input("Enter x co-ordinate:"))
        self.y=int(input("Enter y co-ordinate:"))
    def cal_distance(self,other):
        d=math.sqrt((other.y-self.y)**2+(other.x-self.x)**2)
        return d
          
p1=point(3,5)
#print("Enter first point co-ordinates:")
#p1.get_point()
#p1.print_point()
print(p1)
p2=point(4,7)
#print("Enter second point co-ordinates:")
#p2.get_point()
#p2.print_point()
distance=point.cal_distance(p1,p2)
print("Distance between  points is :{}".format(distance))
