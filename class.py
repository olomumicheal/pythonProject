#conditional statement

#if conditional statement
a = 40
b = 30.5

if a > b:
    print("a is greater than b")

#elif conditional statement
x = 33
y = 33

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")

#else conditional statement
m = 33
n = 50

if m < n:
    print("m is less than n")
elif x == y:
    print("m is equal to n")
else:
    print("m is less than n")

#shorthand if else and ternary operator
q = 20.5
l = 20;
print("welcome") if q > l else print("Not welcome")


#logical operator and, or and not
e = 30
f = 30.5
g = 101

if e > f and g < f:
    print("Both  conditions are true")
else:
    print("Both conditions are not met")

if e > f or g > f:
    print("Both  conditions are true")

if not e > f:
    print("Both  conditions are not true")

#Nested if
x = 50

if x > 10:
    print("x is greater than 10")
    if x < 20:
        print("x is greater than 20")
    else:
        print("x is equal to 50")


#while loop in python
x = 10
while x <= 200:
    print(x)
    x += 10

#using break statement
x = 10
while x <= 200:
    print(x)
    if x == 100:
        break
    x += 10

#using continue statement
x = 10
while x <= 200:
    x += 10
    if x == 100:
        continue
    print(x)

#The else statement
x = 10
while x <= 200:
    print(x)
    x += 10
else:
    print("x is no longer less than 200")


#For loop
fruits = ["Banana", "Mango", "Apple"]
for x in fruits:
    print(x)

#looping through a string
a = "banana"
for x in "banana":
    print(x)


#using break statement
fruits = ["Banana", "Mango", "Apple"]
for x in fruits:
    print(x)
    if x == "Mango":
        break


#functions in python
def myFunction():
    print("Welcome To Atlanta")

myFunction()


#functions with argument
def nameFunction(fnamne):
    print("my names are " + fnamne)

nameFunction("Tobias")
nameFunction("Maxwell")
nameFunction("Solomon")

#numbers of argument
def fullNameFunction(fname, lname):
    print(fname + " " + lname)

fullNameFunction("Micheal", "Oladi")


#Arbitrary Argument
def myfunction(*child):
    print("The youngest child is " + child[1])

myfunction("james", "lucifer", "cain")

#keyword argument
def myfunc(kid1, kid2, kid3):
    print("Baby " + kid2 + " is way to young.")

myfunc(kid1 = "james", kid2="lawrence", kid3="blahbablue")

#passing list as an argument
def myfunct(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "orange"]
myfunct(fruits)


#return method
def Return(a):
    return 5 * a

print(Return(5))
print(Return(10))
print(Return(20))