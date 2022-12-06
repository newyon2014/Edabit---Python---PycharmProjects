def all_truthy(*args):
    for i in args:
        if not bool(i):
            return False
        else:
            return True
