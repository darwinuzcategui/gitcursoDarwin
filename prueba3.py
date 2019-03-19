
import json

xJson = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#print(json.dumps(x))
#import json
"""
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("--------4 de identacio-------------------------------------")
print(json.dumps(xJson, indent=4))
#You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, 
#and a colon and a space to separate keys from values:

#Example
#Use the separators parameter change the default separator:
print("--------4 de identacio--- separador----------------------------------")

print(json.dumps(xJson, indent=4, separators=(". ", " = ")))
#Order the Result
#The json.dumps() method has parameters to order the keys in the result:
#Example
#Use the sort_keys parameter to specify if the result should be sorted or not:
print("--------4 de identacio--- separador-------- ordenado--------------------------")

print(json.dumps(xJson, indent=4, sort_keys=True))
"""
def myfunc(n):
  return lambda a,b : a * n+b

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11,3)) 
print(mytripler(11,3))
#A lambda function that adds 10 to the number passed in as an argument, and print the result:

x = lambda a : a + 10
print(x(5))
#Lambda functions can take any number of arguments:

#Example
#A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b
print(x(5, 6))

#Example
#A lambda function that sums argument a, b, and c and print the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
 
#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n
#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
#Or, use the same function definition to make a function that always triples the number you send in:

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

#Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))











