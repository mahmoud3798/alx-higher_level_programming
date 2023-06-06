#!/usr/bin/python3
def uppercase(ch):
    result = ""
    for l in ch:
        if ord(l) >= 97 and ord(l) <= 122:
            result += "{:c}".format(ord(l) - 32)
        else:
            result += "{:c}".format(ord(l))
    print(result)
