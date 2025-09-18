def add(*args):
    sum=0
    for i in args:
        print(i)
        sum=sum+i
    return sum


print("Addition of two numbers is:",add(2,5,6,7,8,9))
print("Addition ofthree numbers is:",add(2,5,6))
print("Addition of four numbers is:",add(4,6,7,8))
