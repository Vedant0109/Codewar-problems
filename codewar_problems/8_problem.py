def roman_to_int()-> int:
    """
    Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
    You don't need to validate the form of the Roman numeral.

    Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
    starting with the leftmost digit and skipping any 0s.
    For example:
    - 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC).
    - 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
    - The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
    """

    roman_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_number = "MDCLXVI"
    number = 0

    for romans in roman_number:
        if romans in roman_value:
            roman = roman_value[romans]
            number += roman
        else:
            print("This is not a valid Roman numeral")
            break

    print(f"The number is {number}")


roman_to_int()