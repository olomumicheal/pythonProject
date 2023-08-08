#Python Conditional Statement
#If Statement

# a = 134
# b = 100
#
# if a < b:
#     print("a is less than b")
# else:
#     print("b is greater than a")

# a = 100
# b = 100
#
# if a < b:
#     print("a is less than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")

#AND CONDITION

# a = 200
# b = 30
# c = 400
#
# if a < b and c < b:
#     print("Both conditions are true")
# else:
#     print("Both conditions are false")


#While loop
# i = 2
#
# while i < 9:
#     print(i)
#     i += 2


"""
            ASSESSMENT
1. print out an elif conditional statement of x is equal to y
2. print out an if statement with an and condition of b is less than a and c is less than a
3. print out a while loop statement of i < 12
"""

#Break Statement
# i = 2
#
# while i < 9:
#     print(i)
#     if i == 6:
#         break
#     i += 2
#
# #Continue Statement
# i = 2
#
# while i < 9:
#     i += 2
#     if i == 6:
#         continue
#     print(i)


#For Loop

# fruits = ["Mango", "Apple", "Orange"]
# for x in fruits:
#     print(x)
#
#
# # for i in range(10):
# #     print(i)
# #     i = 5
#
# fruits = ["Mango", "Apple", "Orange"]
# for x in fruits:
#     print(x)
#     if x == "Apple":
#         break


#Classes and Inheritance
#     x = 5
#
# p1 = myClass()
# print(p1.x)

# class Person:e
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("Smuel", 25)
# print(p1.name)
# print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)