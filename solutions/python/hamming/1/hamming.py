def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance = 0
    for value_1, value_2 in zip(strand_a, strand_b):
        if value_1 != value_2:
    # for value in range(len(strand_a)):
    #     if strand_a[value] != strand_b[value]:
            distance += 1
    return distance
