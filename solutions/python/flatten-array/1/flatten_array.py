def flatten(iterable):
    flatten_list = []
    for item in iterable:
        if isinstance(item, list):
            flatten_list.extend(flatten(item))
        elif item is not None:
            flatten_list.append(item)
    return flatten_list

