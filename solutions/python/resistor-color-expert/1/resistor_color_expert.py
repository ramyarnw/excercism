def resistor_label(colors):
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

    tolerance = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }

    band_count = len(colors)

    if band_count == 1:
        return "0 ohms"

    elif band_count == 4:
        first = color_codes[colors[0]]
        second = color_codes[colors[1]]
        multiplier = color_codes[colors[2]]
        tolerance_value = tolerance[colors[3]]

        base = first * 10 + second
        resistance = base * (10 ** multiplier)

    else:
        first = color_codes[colors[0]]
        second = color_codes[colors[1]]
        third = color_codes[colors[2]]
        multiplier = color_codes[colors[3]]
        tolerance_value = tolerance[colors[4]]

        base = first * 100 + second * 10 + third
        resistance = base * (10 ** multiplier)

    if resistance >= 1_000_000_000:
        value = resistance / 1_000_000_000
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        value = resistance / 1_000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"

    if value == int(value):
        value_str = str(int(value))
    else:
        value_str = str(round(value, 2))

    return f"{value_str} {unit} {tolerance_value}"
