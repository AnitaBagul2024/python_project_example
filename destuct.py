class Employee:
  
    # Initializing 
    def __init__(self):
        print('Employee created')
  
    # Calling destructor
    def __del__(self):
        print("Destructor called")
  

  
print('Calling Create_obj() function...')
obj = Employee()
print('Program End...')
del obj
