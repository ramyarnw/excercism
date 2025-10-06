def square_root(number):
    if number < 0:
        return 0
        # linear search
    # i = 1
    # while i * i <= number:
    #     if i * i == number:
    #         return i
    #     i += 1
    # return -1

    # binary search
    min = 1
    max = number
    while min <= max:
        mid = (min + max) // 2
        mid_square = mid * mid
        if mid_square == number:
            return mid
        elif mid_square <= number:
            min = mid + 1
        else:
            max = mid - 1
    return -1
        
    
