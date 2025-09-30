def value(colors):
    color_codes = [
        "black",   
        "brown",   
        "red",    
        "orange",  
        "yellow",  
        "green",  
        "blue",    
        "violet",  
        "grey",    
        "white"    
    ]

    first_digit = color_codes.index(colors[0])
    second_digit = color_codes.index(colors[1])

    return first_digit * 10 + second_digit
