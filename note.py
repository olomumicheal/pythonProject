"""
Python Operators
1. Arithmetic Operator
2. Assignment Operator
3. Comparison Operator
"""

#Arithnetic Operators
addition = 5 + 5
subtraction = 10 - 5
multiplication = 10 * 5
division = 10 / 2

print(addition)
print(subtraction)
print(multiplication)
print(division)


#assignment and comparison operators
age = 18

if age == 20:
    print("Age is equal to 20")
else:
    print("age is less than 20")

#List
names = ["Micheal", "Daniel", "Solomon", "Samson", True, False, 30, 40.5]
print(names)

#Accesiing of list
print(names[4])

#Accesing range of list
print(names[2:5])

#Changing List Item
names[4] = "Samuel"
print(names)

#Adding List Item
names.append("James")
print(names)

names.insert(1, "Mustapha")
print(names)

#Removing list items using remove()
names.remove("Mustapha")
print(names)


#Removing list items using pop()
names.pop(3)
print(names)



