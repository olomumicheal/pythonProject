# import platform

# x = platform.system()
# print(x)


# y = dir(platform)
# print(y)

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
