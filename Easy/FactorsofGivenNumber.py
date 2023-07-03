def find_factors(n):
    new_list = []
    i = 1
    if n == 0:
        return []
    else:
        while n >= i:
            if n % i == 0:
                new_list.append(i)
            i += 1
    return new_list