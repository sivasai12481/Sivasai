'''
#string
x = "Hello World"
#int
x = 20
#float
x = 20.5
#complex
x = 1j
#list
x = ["apple", "banana", "cherry"]
#tuple
x = ("apple", "banana", "cherry")
#range
x = range(6)
#dictinary
x = {"name" : "John", "age" : 36}
#set
x = {"apple", "banana", "cherry"}
#frozen set
x = frozenset({"apple", "banana", "cherry"})
#bool
x = True
#bytes
x = b"Hello"
#bytearray
x = bytearray(5)
#memoryview
x = memoryview(bytes(5))
#None
x = None



print ("setting the specific data type")
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)	
x = list(("apple", "banana", "cherry"))	
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)		
x = bytes(5)		
x = bytearray(5)
x = memoryview(bytes(5))


print("python Numbers")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#float
x = 1.10
x = 35e3


print("conversion from one type to another type")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

'''

import random
print(random.randrange(1,5))
