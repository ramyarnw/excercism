import operator
import math
def convert(number):
    result = ""
    
    if operator.mod(number,3) == 0:
        result += "Pling"
    if math.fmod(number,5) == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    
    if result == "":
        return str(number)
    
    return result
