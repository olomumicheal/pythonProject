#lambda
x = lambda a: a + 20

print(x(10))

#lambda with two or more qrgument
x = lambda a, b: a * b
print(x(5, 6))
x = lambda  a, b, c: a + b + c
print(x(3, 4, 5))

#lambda functions
def myFunction(n):
    return lambda a: a * n

mydoubler = myFunction(2)
mytrippler = myFunction(3)

print(mydoubler(20))
print(mytrippler(30))


#ojects with classes/oject
class newClass:
    x = 10

p1 = newClass()
print(p1.x)


#class using init()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x1 = Person("John Doe", "25")

print(x1.name)
print(x1.age)

print(x1.name + " is " + x1.age + " years old" )

#class using
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"

x1 = Person("John Doe", 25)

print(x1)

#Object method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunction(self):
        print("Hello! my name is " + self.name)

x1 = Person("John Doe", 25)
x1.myfunction()

#The self parameter method
class Person:
    def __init__(micheal, name, age):
        micheal.name = name
        micheal.age = age
    def myfunction(samuel):
        print("Hello! my name is " + samuel.name)

x1 = Person("James Hamburger", 25)
x1.myfunction()


#Inheritance
class mySchool:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printdata(self):
        print(self.firstName, self.lastName)

x1 = mySchool("James", "John")
x1.printdata()

#Inheritance  between the parent and the child
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lname = lname

    def printdata(self):
        print(self.firstName, self.lname)

class Student(Person):
    pass

xa = Student("John", "Kelvin")
xa.printdata()




