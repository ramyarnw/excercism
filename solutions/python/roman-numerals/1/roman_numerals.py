def roman(number):
    if 0 < number > 4000:
        raise ValueError("Number must be between 1 and 3999")

    roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    result = ""
    for key, value in roman_map:
        while number >= key:
            result += value
            number -= key
    return result

