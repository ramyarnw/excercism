def factors(value):
    factors = []
    while value % 2 == 0:
        factors.append(2)
        value //= 2
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor += 2 
    if value > 1:
        factors.append(value)

    return factors
