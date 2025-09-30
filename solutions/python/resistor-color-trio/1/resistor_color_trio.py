def label(colors):
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    first_digit = color_codes[colors[0]]
    second_digit = color_codes[colors[1]]
    multiplier = color_codes[colors[2]]

    base_value = first_digit * 10 + second_digit
    resistance = base_value * (10 ** multiplier)

    if resistance>= 1000000000:
        return f"{resistance // 1000000000} gigaohms"  
    if resistance>= 1000000:
        return f"{resistance // 1000000} megaohms"
    if resistance >= 1000 <= 1000000:
        return f"{resistance // 1000} kiloohms"
    else:
        return f"{resistance} ohms"
