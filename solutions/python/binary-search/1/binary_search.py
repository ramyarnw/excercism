def find(search_list, value):
    min = 0
    max = len(search_list) - 1
    while min <= max:
        mid = (min + max) // 2
        guess = search_list[mid]
        if guess == value:
            return mid
        elif guess < value:
            min = mid + 1
        else:
            max = mid - 1
    raise ValueError("value not in array")
