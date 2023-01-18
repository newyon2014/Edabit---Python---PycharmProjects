def last_ind(lst):
    if len(list(lst)) == 0 or len(str(lst)) == 0:
        return None
    return list(lst).pop()