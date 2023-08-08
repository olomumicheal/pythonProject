# import platform
#
# x = platform.system()
# print(x)
#
# x = dir(platform)
# print(x)
import json
import math

# import datetime
#
# x = datetime.datetime.now()
# print(x)
#
# print(x.year)
# print(x.strftime("%A"))

# importing the required module
import matplotlib.pyplot as plt
#
# # x axis values
x = [1, 2, 3]
# # corresponding y axis values
y = [2, 4, 1]
#
# # plotting the points
plt.plot(x, y)
#
# # naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
#
# # giving a title to my graph
plt.title('My first graph!')
#
# # function to show the plot
plt.show()

# Built in Math function
x = min(2, 4, 5)
y = max(5, 6, 9)
print(x)
print(y)

#Math module
x = math.sqrt((64))
y = math.ceil(4.5)
z = math.floor(4.5)
a = math.pi
print(x)
print(x)
print(y)
print(z)
print(a)

#converting json to python dictionary
# import json
# x = '{"name": "james", "age": 25, "isMarried": False}'
# #
# y = json.loads(x)
# print(y["age"])

# import json
#
# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])
#
# x = {
#     "name": "john",
#     "age": 25
# }
#
# y = json.dumps(x)
# print(y)


import camelcase

x = camelcase.CamelCase()

txt = "welcome to bizmarrow"

print(x.hump(txt))

