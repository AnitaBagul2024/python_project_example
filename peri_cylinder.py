#python program to find the perimeter of cylinder
#Formula : Perimeter of cylinder ( P ) =( 2 * d ) + ( 2 * h )
#here d is the diameter of the cylinder h is the height of the cylinder

def perimeter( diameter, height ) : 
    return 2 * ( diameter + height )  
  
 
diameter = 5 ; 
height = 10 ; 
print ("Perimeter = ",perimeter(diameter, height)) 
