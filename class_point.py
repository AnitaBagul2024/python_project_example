import math
class point():
    """x,y"""
    def print_point(p):
        print("{},{}".format(p.x,p.y))
    def get_point(p):
        p.x=int(input("Enter x co-ordinate:"))
        p.y=int(input("Enter y co-ordinate:"))
    def cal_distance(p1,p2):
        d=math.sqrt((p2.y-p1.y)**2+(p2.x-p1.x)**2)
        return d
class point1():
    """a,b"""
          
p1=point()
print("Enter first point co-ordinates:")
p1.get_point()
p1.print_point()
print(type(p1))
p2=point()
print("Enter second point co-ordinates:")
p2.get_point()
p2.print_point()
distance=point.cal_distance(p1,p2)
print("Distance between  points is :{}".format(distance))




#p3=point1()
#get_point(p3)
