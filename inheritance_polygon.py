class polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
        print(self.sides)
    def inputsides(self):
        self.sides=[float(input("Enter sides"+str(i+1)))for i in range(self.n)]

    def checkside_list(self):
        print(self.sides)
        
    def displaysides(self):
        
        for i in range(0,self.n):
            print("sides",i+1,"is",self.sides[i])
            
class triangle(polygon):
    def __init__(self):
        super().__init__(3)
    def area(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("Area of triangle is:",area)
class square(polygon):
    def __init__(self):
        polygon.__init__(self,1)
    def area1(self):
        a=self.sides[0]
        area=a**2
        print("Area of square is:",area)
        
        
print(__name__)   #main
t=triangle()
t.inputsides()
t.checkside_


list()
t.displaysides()
t.area()

sq=square()
sq.inputsides()
sq.displaysides()
sq.area1()
