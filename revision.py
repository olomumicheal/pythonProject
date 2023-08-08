#print("Hello World")

"""
Data types in Python
1. String data type
2. Numeric Data type (int and float)
3. List
4. Tuple
5. Set
6. Dictionary
7. Boolean
"""

#string data type
firstName = "Micheal"
lastName = "Samuel"
print(firstName)
print(lastName)

#concatenation of variables
fullName = firstName + " " + lastName
print(fullName)

#concatenating strings and variables
print("Hello " + fullName + " how are you?")

#Numeric Data type
x = 200
y = 40

#Arithmetic Numeric operation
a = x * y
b = x - y

#Comparison Numeric operation
if x == y:
    print("x is qual to y")
else:
    print("x is greater than y")


#Boolean data type
ismarried = True
isMarried = False
print(isMarried)
print(ismarried)
print(type(ismarried))


#List Data type
myDatas = ["fruits", "schools", 20.5, 140, False]
print(myDatas)
print(type(myDatas))

#Tuple data type
mytuple = ("mango", "orange", "ministry", 300, 50.6, True)
print(mytuple)
print(type(mytuple))

#Set data type
mySet = {"secondary", "university", "polytechnic", 600, 7.05, True}
print(mySet)
print(type(mySet))

#Dictionary data type
myDictionary = {
    "firstName": "Samuel",
    "lastName": "Micheal",
    "state": "Ondo",
    "age": 25,
    "isMarried": False,
    "myFavGames": ["Football", "Basketball", "Volleyball"],
    "myFavFood": ("jollof", "spicy")
}

print(myDictionary)
print(type(myDictionary))


"""
                    ASSESSMENT
1. declare a variable of a string data, the ouput of concatenation between the variables and the strings shoild be "Welcome to Nigeria, 
a country located in Africa.
2. create a dictionary with tyhe following details; a boolean, a set data, a list dat and a float data
3. using a conditional statement with comparison operation; output a is less than b
4. what do you understand by accessing and adding data to a list data type
5. how do you access a tuple data

Note: 4 and 5 should practicalized with codes.
"""