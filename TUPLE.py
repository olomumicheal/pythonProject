#Confirming the tuple data type
mySchools = ("Primary", "Secondary", "Tertiary", True, 25, 0.5)
print(mySchools)
print(type(mySchools))

#How to Access Tuple
print(mySchools[2])
print(mySchools[2:4])

#How to update Tuple
x = ("Mango", "Strawberry", "Chocolate")
y = list(x)
y[1] = "Pineaple"
x = tuple(y)
print(x)

#Joining two tuples
tuple1 = ("Crayfish", "Arrays", "Phenomena", "History")
tuple2 = (50, 0.5, True, False)

tuple3 = tuple1 + tuple2
print(tuple3)


#Set Data Type
mySet = {"hOME aLONE", "Candidate", "Veldora", "Grace"}
print(mySet)
print(type(mySet))

#How to access set
for x in mySet:
    print(x)

#Confirming the set data
print("Candidate" in mySet)



"""
                    ASSESSMENT
1. print out a list data and confirm the data type using type()
2. print out a tuple data and confirm the data type using type()
3. print out a set data and confirm the data type using type()
4. For each data created above, add them with a new data type to give it a join method
5. concatenate a string and a variabl of your choice
"""