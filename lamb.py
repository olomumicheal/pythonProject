#Python Lambda
x = lambda a: a + 10
print(x(5))

#lambda with argument
x = lambda a, b: a * b
print(x(5, 7))


#lambda with multiple argument
x = lambda a, b, c: a + b + c
print(x(3, 4, 5))

#combining lambda and function
def myFunc(n):
    return lambda a: a * n

mytripler = myFunc(3)
print(mytripler(10))

def myfunc(m):
    return lambda a: a * m

myDoubler = myfunc(2)
myTripler = myfunc(3)

print(myDoubler(10))
print(myTripler(10))


#Classes and Object
class myClass:
    x = 5
x1 = myClass()
print(x1.x)


#Classes with init()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 30)

print(p1.name)
print(p1.age)

#Class with Object method
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello, my name is " + self.name)

p1 = Human("Clement", 28)
p1.myFunc()

"""
                        ASSESSMENT
1. def a function to print "Welcome To Atlanta"
2. def a function to return y * 5 and y * 0.5
3. using lambda method call out three argument multiplying each other.
"""