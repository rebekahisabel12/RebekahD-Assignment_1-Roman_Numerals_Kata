def whole_number_to_roman_numeral(num):
    if num < 1 or num > 5:
        print("Does not exist")

    small_numbers = {
        1: 'i',
        2: 'ii',
        3: 'ii'
    }

    return small_numbers[num]


converter = int(input("Enter whole number: "))

result = whole_number_to_roman_numeral(converter)

print(f"Whole Number: {converter}, Roman Numeral: {result}")
