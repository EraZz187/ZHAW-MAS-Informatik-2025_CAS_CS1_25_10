# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 2016: c=21, d = 2507, e = 21, g = 3, x = 3, y = 2016, z = 1

y = int(input("Geben sie das Jahr ein "))

g = (y % 19) + 1
c = int(y / 100) + 1
x = int(3 * c / 4) - 12
z = int((8 * c + 5) / 25) - 5
d = int(5 * y / 4) - x - 10
e = (11 * g + 20 + z - x) % 30

if (e == 25 and g > 11) or e == 24:
    e = e + 1

n = 44 - e
if n < 21:
    n = n + 30

n = n + 7 - ((d + n) % 7)

if n > 31:
    print(str(n -31) + " APRIL")
else:
    print(str(n) + " MARCH")
