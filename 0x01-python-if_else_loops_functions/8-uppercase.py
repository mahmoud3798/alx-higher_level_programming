#!/usr/bin/python3
def uppercase(ch):
    result = ""
    for c in ch:
        if ord(c) >= 97 and ord(c) <= 122:
            result += "{:c}".format(ord(c) - 32)
        else:
            result += "{:c}".format(ord(c))
    print(result)
