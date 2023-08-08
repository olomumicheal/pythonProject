#creating a dictionary
myDetails = {
    "firstName": "Michael",
    "lastName": "Samuel",
    "age": 25,
    "isMarried": False,
    "myFavGame": ["Football", "Volleyball", "Basketball"]
}

print(myDetails)

#Accessing Dictionary
x = myDetails["firstName"]
print(x)

#using keys() method
x = myDetails.keys()
print(x)

#using values() method
x = myDetails.values()
print(x)

#using item() method
x = myDetails.items()
print(x)

if "age" in myDetails:
    print("age key is in myDetails")

#change an item
myDetails["age"] = 27
print(myDetails)

#using update()
myDetails.update({"lastName": "Olaoluwa"})
print(myDetails)

myDetails.update({"myFavFun": {"swimming", "flying"}})
print(myDetails)


#How to remove an item from a dictionary
myDetails.pop("firstName")
print(myDetails)

myDetails.popitem()
print(myDetails)

del myDetails["lastName"]
print(myDetails)

#looping through dictionary
#loop through keys
for x in myDetails:
    print(x)

for x in myDetails.keys():
    print(x)

#loop through values
for x in myDetails:
    print(myDetails[x])

for x in myDetails.values():
    print(x)

#Nested Dictionaries
myFamily = {
    "chaild1": {
        "FullName": "Sunday James",
        "age": 15
    },

    "child2": {
        "FullName": "Christopher James",
        "age": 17
    },

    "child3": {
        "FullName": "Mary Rose",
        "age": 20
    }
}

print(myFamily)

child1 = {
        "FullName": "Sunday James",
        "age": 15
    }

child2 = {
        "FullName": "Christopher James",
        "age": 17
    }

child3 = {
        "FullName": "Mary Rose",
        "age": 20
    }

myFamilies = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myFamilies)