def calculate(num1, num2, op):
    if op.__eq__("+"):
        return num1 + num2
    elif op.__eq__("-"):
        return num1 - num2
    elif op.__eq__("*"):
        return num1 * num2
    elif op.__eq__("//"):
        return num1 // num2
    elif op.__eq__("%"):
        return num1 % num2
    else:
        return num1 / num2