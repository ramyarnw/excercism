from itertools import combinations as it_combinations
def combinations(target, size, exclude):
    exclude = set(exclude)
    digits = [d for d in range(1, 10) if d not in exclude]
    valid_list = []
    for combi in it_combinations(digits, size):
        if sum(combi) == target:
            valid_list.append(list(combi))
    return sorted(valid_list)
            
