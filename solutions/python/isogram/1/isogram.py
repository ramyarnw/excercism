def is_isogram(string):
    found_letters = set()
    string = string.lower()
    for char in string:
        if 'a'<= char <= 'z':
            if char in found_letters:
                return False
            found_letters.add(char)
    return True
