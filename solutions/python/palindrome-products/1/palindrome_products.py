def largest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    largest_palindrome = None
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j

            # Stop early if product is already less than current max
            if largest_palindrome is not None and product < largest_palindrome:
                break

            if str(product) == str(product)[::-1]:  # Check palindrome
                if largest_palindrome is None or product > largest_palindrome:
                    largest_palindrome = product
                    factors = [(j, i)]
                elif product == largest_palindrome:
                    factors.append((j, i))

    return (largest_palindrome, factors)

def smallest(max_factor, min_factor=0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    smallest_palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j

            if smallest_palindrome is not None and product > smallest_palindrome:
                break

            if str(product) == str(product)[::-1]:
                if smallest_palindrome is None or product < smallest_palindrome:
                    smallest_palindrome = product
                    factors = [(i, j)]
                elif product == smallest_palindrome:
                    factors.append((i, j))

    return (smallest_palindrome, factors)
