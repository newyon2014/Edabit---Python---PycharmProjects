def int_within_bounds(n, lower, upper):
    return False if isinstance(n, int) == False else upper > n >= lower