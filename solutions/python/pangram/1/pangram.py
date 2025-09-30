def is_pangram(sentence):
    sentence = sentence.lower()
    found_letters = set()
    for char in sentence:
        if 'a' <= char <= 'z':
            found_letters.add(char)
        if len(found_letters) == 26:
            return True 
    return len(found_letters) == 26
