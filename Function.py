#Python Functions

#Calling a function output
def myFunc():
    print("Welcome To Atlanata")

myFunc()

def micheal():
    print("Micheal how are you")

micheal()

#Defininig functions with argument
def my_function(fname):
    print(fname + " Olomu")

my_function("Micheal")

#Functions with multiple argument
def myFunctions(fname, lname):
    print(fname + lname + " is 25 years old")

myFunctions("Micheal", " Olomu")

#Using Arbitrary Method in Function
def myFunction(*kids):
    print("The first kid by the name " + kids[2] + " is intelligent")

myFunction("James", "Samuel", "Kosy", "Bob", "Mark")

#Using keyword argument
def myfunc(child1, child2, child3):
    print(child2 + " is dull")

myfunc(child1 = "Samuel", child2="James", child3="Bob")

def name(kid1, kid2, kid3):
    print(kid3 + " is intelligent")

name(kid1 = "john", kid2="Solo", kid3="Bob Marley")

#Functions with default parameter value
def myCountry(country = "Nigeria"):
    print("The country name is " + country)

myCountry("Switzerland")
myCountry("Canada")
myCountry()
myCountry("Spain")
myCountry("Ghana")

#Functions with return statement
def myMaths(x):
    return x * 5

print(myMaths(5))
print(myMaths(2))
print(myMaths(4))
print(myMaths(6))