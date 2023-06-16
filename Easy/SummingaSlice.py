def sum_first_n_nums(lst, n):
    if n == 0:
        return 0
    sum = 0
    counter = 0
    for i in lst:
        sum = sum + i
        counter = counter + 1
        if counter == n:
            break
    return sum