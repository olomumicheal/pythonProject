# print("Hello World")

"""
        Data Types in Python Programming Languange
1. string data
2. int
3. float
4. boolean
5. list
6. tuple
7. set
8. dictionary
"""

#String Data Type
firstName = "Samuel"
lastName = "James"
print(firstName)
print(lastName)

#string concatenation
print("My names are " + firstName + " " + lastName)

#int data (whole numbers)
x = 200
y = 3
print(x)
print(y)

#float (decimal numbers)
a = 30.6
b = 000.7
print(a)
print(b)

#boolean
d = True
print(d)
print(type(d))

#List
myFruits = ["Orange", "Mango", "Banana", 80, 0.23,  False]
print(myFruits)
print(type(myFruits))

#Tuple
myFruits = ("Orange", "Mango", "Banana")
print(myFruits)
print(type(myFruits))

#set
myFruits = {"Orange", "Mango", "Banana"}
print(myFruits)
print(type(myFruits))


#Dictionary data type
myDetails = {
    "firstName": "Samuel",
    "lastName": "Doe",
    "age": 25,
    "isMarried": False,
    "myFavGames": ["Volleyball", "Football", "Basketball"],
    "myFavNumber": {45, 60, 0.78},
    "myFavCountry": ("Brazil", "Canada", "Austria")
}

print(myDetails)
print(type(myDetails))

