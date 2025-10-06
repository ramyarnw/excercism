def abbreviate(words):
    punctuation = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"
    cleaned = words.replace("-", " ")
    cleaned = ''.join(char for char in cleaned if char not in punctuation)
    splitted_words = cleaned.split()
    acronym = ''.join(word[0].upper() for word in splitted_words)
    return acronym
