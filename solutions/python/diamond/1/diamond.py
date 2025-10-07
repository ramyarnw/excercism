def rows(letter):
    size = ord(letter) - ord('A')
    lines = []
    for i in range(size + 1):
        ch = chr(ord('A') + i)
        padding = ' ' * (size - i)
        if ch == 'A':
            line = padding + 'A' + padding
        else:
            inner = ' ' * (2 * i - 1)
            line = padding + ch + inner + ch + padding
        lines.append(line)
    full_diamond = lines + lines[-2 :: -1]
    return list(full_diamond)
