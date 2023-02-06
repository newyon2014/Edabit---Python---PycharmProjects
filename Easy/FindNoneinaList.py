def find_none(lst):
    return -1 if not list(lst).__contains__(None) else list(lst).index(None)
