#tetrahedron
#area formula is area = sqrt(3) * s^2
#Regular Tetrahedron Formula: A regular tetrahedron's area of one face: Area= √3x² (x is side length).
#Total surface area: TSA=4*√3x² and Volume: V= (a³√2) / 12 ​ ​ (a is side length).


import math
 
 
def calculate_tetrahedron_area(side):
    area = math.sqrt(3) * side ** 2 / 4
    return round(area, 2)
 
 
# Example usage:
side = 3
area = calculate_tetrahedron_area(side)
print("The area of a tetrahedron with side", side, "is", area)
