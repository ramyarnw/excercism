def commands(binary_str):
    final_list = []
    # binary_string_formatted = format(binary_str, 'b')
    if binary_str[-1] == '1':
        final_list.append('wink')
    if binary_str[-2] == '1':
        final_list += ['double blink']
    if binary_str[-3] == '1':
        final_list += ['close your eyes']
    if binary_str[-4] == '1':
        final_list += ['jump']
    if binary_str[-5] == '1':
        final_list.reverse()
    return final_list
        
