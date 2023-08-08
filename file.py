print("Hello World")

#Data Types in Python
"""
1. String Data Type
2. Int Data type
3. Float Data type
4. Boolean Data Type
5. List Data type
6. Set Data type
7. Dictionary Data type
8. Tuple Data Type
"""

#String Data Type
firstName = "Micheal"
lastName = "Samuel"
age = 25

print(firstName)
print(type(firstName))
print(lastName)
print(age)
print(type(age))

#Concatenation of variables
fullName = firstName + " " + lastName
print(fullName)

#Concatenation of strings and variables
sentence = "My name is " + firstName + " " + lastName + " and, i am " + str(age) +" years old."
print(sentence)

"""
                Assessment
1. create a variable to print out "Welcome To Atlanta
2. concantenate a string and a variable to print out "I am located in Abuja
"""

#Numeric Data type (int and float)
x = 20
y = 0.5
z = 200

a = x * y
b = z / x
c = x + y + z

print(a)
print(b)
print(c)

#List Data Type
myList = ["Samuel", True, 0.6, 200]
print(myList)
print(type(myList))

#Set Data Type
mySet = {"Orange", "Mango", "Whine", False, 30, 40.6}
print(mySet)
print(type(mySet))

#Tuple Data Type
myTuple = ("Vine", "Arithmetic", True, False, 0.2, 25)
print(myTuple)
print(type(myTuple))