#Tuple data type
myTuple = ("Samuel", "Orange", 34, 0.34, "David")
print(myTuple)
print(type(myTuple))

#Accesng Tuple
print(myTuple[1])

#How to update data in the Tuple
fruit = ("Mango", "Orange", "Banana")
x = list(fruit)
x[1] = "Pineaple"
fruit = tuple(x)
print(fruit)


#How to join tuple
tuple1 = ("Monday", "Tuesday", "Wednesday")
tuple2 = ("Thursday", "Friday", "Saturday", "Sunday")
tupleDays = tuple1 + tuple2
print(tupleDays)


#Set Data Type
mySet = {True, False, "Nkechi", "Ministry", 40.5, 100}
print(mySet)
print(type(mySet))

#Accessing Set
print("Nkechi" in mySet)

#To add a data to the set
fruits = {"Banana", "Orange", "Maggi"}
fruits.add("Pineaple")
print(fruits)

#To add to set data together
x = {20, 35, 67, 0.56}
y = {35, 56, 7.6}

x.update(y)
print(x)


#Using union to add two variables
z = x.union(y)
print(z)

#Dictionary Data Type
personalInfo = {
    "firstName": "Micheal",
    "lastName": "Olomu",
    "age": 25,
    "isMarried": False,
    "myFavColor": ["Green", "Gold", "White"],
    "myDigit": {20, 30.5, 22.7},
    "daysOff": ("Wednesday", "Friday", "Sunday")
}

print(personalInfo)
print(type(personalInfo))

#Accessing Dictionary using get and keys function
x = personalInfo.get("myFavColor")
print(x)

y = personalInfo.keys()
print(y)

#Change Items using normal method
personalInfo["isMarried"] = True
print(personalInfo)

#change items using update method
personalInfo.update({"lastName": "Samuel"})
print(personalInfo)

#Adding an iotem to the dictionary
personalInfo["Activities"] = "Jogging"
print(personalInfo)

#Removing an item from the dictionary
