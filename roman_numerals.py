roman_key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def i2r(converter):
    first_check = None
    for roman_num, integer in roman_key.items():
        if integer == converter:
            return roman_num
        if converter > integer:
            first_check = roman_num

    remaining = converter - roman_key[first_check]
    return first_check + i2r(remaining)


converter = int(input("Enter whole number: "))

result = i2r(converter)

print(f"Whole Number: {converter}, Roman Numeral: {result}")
