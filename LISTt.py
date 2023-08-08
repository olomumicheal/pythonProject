#outputting a list
fruits = ["Fruits", "Mango", "Banana", "Coconut", "Apple"]
print(fruits)

#Accessing the above list item
print(fruits[1])
print(fruits[4])

#Accessing list item using range
print(fruits[2:4])

#check if item exist
if "Cucumber" in fruits:
    print("Yes! Cucumber is in fruits list")
else:
    print(("No! Cucumber is not in this list"))


#How to change list item
fruits[1] = "Blueberry"
print(fruits)

fruits[1:3] = "Guava", "Guavas"
print(fruits)

#How to change using insert()
fruits.insert(2, "raspberry")
print(fruits)


#How to add data to an item
fruits.append("strawberry")
print(fruits)

#using extend method to add two list together
fruit1 = ["peanut", "palmy drink"]
fruits.extend(fruit1)
print(fruits)

#How To remove an item
fruits.remove("palmy drink")
print(fruits)

#How to remove an item using pop()
fruits.pop(3)
print(fruits)


#using del method
del fruits[2]
print(fruits)


#Looping through a list
for x in fruits:
    print(x)

#to get the length of the list
# for i in range(len(fruits)):
#     print(fruits[i])

#sorting a list
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)