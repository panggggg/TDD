def int_to_roman(number):

    nums = [1, 3, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols = [
        "I",
        "III",
        "IV",
        "V",
        "IX",
        "X",
        "XL",
        "L",
        "XC",
        "C",
        "CD",
        "D",
        "CM",
        "M",
    ]

    i = 13
    roman_number = ""

    while number != 0:
        if nums[i] <= number:
            roman_number += symbols[i]
            number = number - nums[i]
        i -= 1
    return roman_number


print(int_to_roman(984))
# for x in range(950, 1001):
#     print(x, int_to_roman(x))