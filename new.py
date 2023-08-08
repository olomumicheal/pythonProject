#Python Dictionary
myDetails = {
    "firstName": "Samuel",
    "LastName": "John",
    "age": 25,
    "isMarried": False,
    "favouriteGames": ["Football", "Basketball", "Tabletennis"],
    "favouriteSubject": ("Maths", "English", "Statistic")
}

print(myDetails)

#Accessing Dictionary using it key name
x = myDetails["favouriteGames"]
print(x)

#Accesing dictionary using get()
y = myDetails.get("favouriteSubject")
print(y)

#Using keys method
z = myDetails.keys()
print(z)

#To add an item to the dictionary
a = myDetails.keys()
print(a)
myDetails["color"] = "white"
print(a)

#To get values
b = myDetails.values()
print(b)


#Change values in dictionary
myDetails["isMarried"] = True
print(myDetails)

#How to update dictionary
myDetails.update({"year": 2020})
print(myDetails)


#Removing an item from the list using pop()
myDetails.pop("favouriteGames")
print(myDetails)

#Removing an item from the list using popitem()
myDetails.popitem()
print(myDetails)

#Using the del keyword
# del myDetails
# print(myDetails)

#Using clear()
myDetails.clear()
print(myDetails)

#Nested Dictionary
myFamily = {
    "child3": {
        "name": "John",
        "age": 18,
        "isMarried": False,
        "faavouriteCounties": ["Canada", "Tokyo"]
    },

    "child2": {
        "name": "Samuel",
        "age": 27,
        "isMarried": True,
        "faavouriteCounties": ["USA", "Morocco"]
    },

    "child1": {
        "name": "Solomon",
        "age": 32,
        "isMarried": True,
        "faavouriteCounties": ["Austria", "Australia"]
    }
}

print(myFamily)