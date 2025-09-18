class abc():
    """x,y"""
    def __str__(self):
        return("%d,%d"%(self.c,self.d))
    
    def __init__(self,c,d=0):
        self.c=c
        self.d=d
        
    def __del__(self):
        print("Object destroyed!!!!!!")
        
    def display(self):
        print("{},{}".format(self.c,self.d))
        
a=abc(56,87)#parameterised constructor
#a.__str__()
#a.display()
print(a)
b=abc(24)#parameterised constructor with single value
#b.__str__()
#b.display()
print(b)
del(a)
#a.__del__()
del(b)
#b.__del__()
