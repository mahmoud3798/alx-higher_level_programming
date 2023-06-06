#!/usr/bin/python3
result = ""
for i in range(100):
    result += "{:02d}".format(i)
    if i != 99:
        result += ", "

print(result)
