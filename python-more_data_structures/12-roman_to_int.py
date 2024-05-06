#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {"M": 1000,
                "D": 500,
                "C": 100,
                "L": 50,
                "X": 10,
                "V": 5,
                "I": 1
                }
    total = 0
    try:
        for i in range(len(roman_string)):
            if i == len(roman_string) - 1:
                total += numerals[roman_string[i]]
                break
            elif numerals[roman_string[i]] < numerals[roman_string[i + 1]]:
                total -= numerals[roman_string[i]]
            else:
                total += numerals[roman_string[i]]
    except TypeError:
        pass
    return total
