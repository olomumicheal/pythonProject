#Two types of loops; The while loop and the For loop

#While loop
i = 1
while i < 6:
    print(i)
    i += 1

#Using break statement in while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Using Continue Statement in while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Using else condition in while loop
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


#Python For Loops
fruits = ["Mango", "Orange", "Vegetable"]
for x in fruits:
    print(x)

#Looping through a string
y = "banana"
for x in "banana":
    print(x)

#Functions in Python
def myFunction():
    print("Welcome To Bizmarrow Technology")
myFunction()


#Introducing parameters to conditional statement
def myFunction(firstName, lastName):
    print("my name is " + firstName + " " + lastName)

myFunction("Micheal", "Samuel")


#Functions with constant declaration
def myFunc(country = "Nigeria"):
    print("My country is " + country)

myFunc("Switzerland")
myFunc("Canada")
myFunc("Australia")
myFunc()
myFunc("Algeria")


#Function with return statement
def myfunc(x):
    return x * 5

print(myfunc(10))
print(myfunc(2))
print(myfunc(5))