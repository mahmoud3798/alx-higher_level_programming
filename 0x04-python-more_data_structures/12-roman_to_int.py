#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    result = 0
    r_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for indx in range(len(roman_string)):
        i = r_dic.get(roman_string[indx])
        if (indx < len(roman_string) - 1):
            h = r_dic.get(roman_string[indx + 1])
            if h > i:
                result -= i
            else:
                result += i
        else:
            result += i
    return (result)
