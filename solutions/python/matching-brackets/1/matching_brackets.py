def is_paired(input_string):
    matching = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = []  

    for ch in input_string:
        if ch in '([{':
            stack.append(ch)
        elif ch in matching:
            if not stack:
                return False
            top = stack.pop() 
            if matching[ch] != top:
                return False
    return len(stack) == 0
