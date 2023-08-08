#List of fruits
myFruits = ["Orange", "Banana", "pineaple", "cherry"]
print(myFruits)
print(type(myFruits))

#Accessing List Item
print(myFruits[1])

#Accesing data in list using range method
print(myFruits[1:3])

#Changing data in a list item
myFruits[2] = "Mango"
print(myFruits)

#Changing list item using range method
myFruits[1:3] = ["Guava", "Apple"]
print(myFruits)

#Adding a data to the list using append()
myFruits.append("Blackberry")
print(myFruits)

#Adding a data to the list using insert()
myFruits.insert(1, "Blueberry")
print(myFruits)

#Using extend method to add two different list
fruit1 = ["Mango", "Pineaple", "Apple"]
fruit2 = ["Orange", "Blueberry"]
fruit1.extend(fruit2)
print(fruit1)

#Removing an item from the list using remove()
fruit3 = ["Mango", "Pineaple", "Apple", "Orange", "Blueberry"]
fruit3.remove("Apple")
print(fruit3)

#Using pop()
fruit3.pop(3)
print(fruit3)