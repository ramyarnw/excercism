def is_armstrong_number(number):
    digits = str(number)
    number_digits = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** number_digits
    return total == number


        

