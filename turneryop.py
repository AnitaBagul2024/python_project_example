x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
max=x if x>y and x>z else y if y>z and y>x else z
print("{} is maximum".format(max))
