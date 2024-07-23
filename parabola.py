#The standard form of a parabola equation is y=ax^2+bx+c. Input the
#values of a, b and c, our task is to find the coordinates of the vertex,
#focus and the equation of the directrix.
'''
For a parabola in the form y=ax^2+bx+c
Vertex: (-b/2a, 4ac-b^2/4a)
Focus: (-b/2a, 4ac-b^2+1/4a)
Directrix: y=c-(b^2+1)4a'''


def findparabola(a, b, c):
    
   print ("Vertex: (" , (-b / (2 * a)) , ", ",(((4 * a * c) - (b * b)) / (4 * a)) , ")" )
   print ("Focus: (" , (-b / (2 * a)) , ", ", (((4 * a * c) -(b * b) + 1) / (4 * a)) , ")" )
   print ("Directrix: y=", (int)(c - ((b * b) + 1) * 4 * a ))


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

#a = 7
#b = 5
#c = 3
findparabola(a, b, c)
