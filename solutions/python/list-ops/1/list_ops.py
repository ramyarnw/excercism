def append(list1, list2):
    result = []
    for x in list1:
        result.append(x)
    for y in list2:
        result.append(y)
    return result

def concat(lists):
    result = []
    for list in lists:
        result.extend(list)
        # result = append(result, list)
    return result

def filter(function, list):
    result = []
    for x in list:
        if function(x):
            result.append(x)
            # result += [x]
    return result

def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

def map(function, list):
    result = []
    for x in list:
        result.append(function(x))
        # result += [function(x)]
    return result

def foldl(function, list, initial):
    acc = initial
    for x in list:
        acc = function(acc, x)
    return acc

def foldr(function, list, initial):
    if not list:
        return initial
    head = list[0]
    tail = list[1:]
    acc_tail = foldr(function, tail, initial)
    return function(acc_tail, head)

def reverse(list):
    result = []
    for x in list:
        result = [x] + result
    return result
