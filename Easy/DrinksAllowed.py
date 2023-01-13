def should_serve_drinks(age, on_break):
    return True if on_break is False and age >= 18 else False
