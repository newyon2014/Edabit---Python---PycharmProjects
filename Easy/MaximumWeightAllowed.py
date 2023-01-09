def weight_allowed(car, p, max_weight):
    return round((car + sum(p)) * 0.453592) < max_weight
