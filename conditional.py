""""
Conditional Statement
Equals                           a == b
Not Equal to                     a != b
less than                        a < b
greater than                     a > b
less than or equal to           a <= b
greater than or equal to        a >= b
"""

"""
We have three types of conditional statement
1. if           #if conditional statement only works when a condition is true
2. Elif         #Elif conditional statement only works when the condition for if or else is not meant
3. Else         #Else conditional statement only works when the condition for if is not meant
"""


#IF  & ELSE Conditional statemnt
x = 20
y = 0.5

if x == y:
    print("x is equal to y")
else:
    print("x is greater than y")

#ELIF Conditional Statement
a = 25
b = 250

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")


#Using AND logical statement

a = 20
b = 30
c = 0.5

if a > b and b < c:
    print("both conditions are true")
else:
    print("both conditions are not true")

#AND logical statement only works when both conditions are true
x = 200
y = 20
z = 300

if x > y and z > x:
    print("both conditions are true")
else:
    print("both conditions are false")

#OR logical statement
m = 40
n = 30
o = 0.5

if m > n or n < o:
    print("One of the condition is true")
else:
    print("None of the conditions is true")


#Using not conditional statement
a = 22
b = 3

if not a > b:
    print("a is greater than b")

else: print("a is less than b")