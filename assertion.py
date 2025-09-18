#try...assert..except example

x="goodbye"
try:
    assert x=="hello","no"
    #assert x=="goodbye","x should be 'hello'"
except AssertionError as e:
    print(e)
    
print("I am always here")
