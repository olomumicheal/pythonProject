#declaring a list data type
mylist = ["fruits", "Ministry", "Force", 200, 0.45, True]
print(mylist)

#Accessing a list item
print(mylist[2])
print(mylist[-1])
print(mylist[0:6])


#changing list item
mylist[3] = "Grey"
print(mylist)

mylist[1:3] = ["Banana", "Mango"]
print(mylist)

#Adding a data to the list using append, insert and tropical
mylist.append("Fuel")
print(mylist)

mylist.insert(2, "kerosine")
print(mylist)

newlist = ["Bizmarrow", "Company"]
mylist.extend(newlist)
print(mylist)

#How to delete an item from a list
mylist.remove("kerosine")
print(mylist)

mylist.pop()
mylist.remove(0.45)
print(mylist)


#Looping through a list
# for y in mylist:
#     print(y)

#sort a list
mylist.pop(4)
print(mylist)

mylist.sort()
print(mylist)

#sorting in descending order
mylist.sort(reverse=True)
print(mylist)

#joining two list data
seconddata = ["Pi", "Zero", True]
thirddata = mylist + seconddata
print(thirddata)

#using looping method to add data
for x in seconddata:
    mylist.append(x)

print(mylist)