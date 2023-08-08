#Accessing a Dictionary

myDict = {
    "fname": "John",
    "lname": "Doe",
    "age": 25
}

print(myDict)

x = myDict["lname"]
print(x)

#using the get()
y = myDict.get("age")
print(y)

#How to get the keys data
z = myDict.keys()
print(z)

#How to get the key values
a = myDict.values()
print(a)


#Changing an item
myDict["age"] = 45
print(myDict)

#using update() to change an item
myDict.update({"lname": "samuel"})
print(myDict)

#To add an item
myDict["isMarried"] = False
print(myDict)

#Removing an Item from the list
myDict.pop("age")
print(myDict)

#using popitem()
myDict.popitem()
print(myDict)

#using del keyword
del myDict["lname"]
print(myDict)

#using clear()
myDict.clear()
print(myDict)


#looping through a dict
newDict = {
    "fname": "bizmarrow",
    "lanme": "Technology",
    "years": 10
}

#To return the keys via loop
for x in newDict:
    print(x)

for x in newDict.keys():
    print(x)

#To return the values via loop
for x in newDict:
    print(newDict[x])

for x in newDict.values():
    print(x)

#To print both keys and values
for x, y in newDict.items():
    print(x, y)


#Nested Dictionary

myChildren = {
    "child1": {
        "fullname": "james",
        "age": 10
    },

    "child2": {
        "fullname": "sampson",
        "age": 12
    }
}

print(myChildren)



