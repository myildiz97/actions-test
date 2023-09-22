def add(a, b):
    if a is None or b is None:
        raise ValueError(f'Missing value: a={a}, b={b}')
    return a + b

def subtract(a, b):
    if a is None or b is None:
        raise ValueError(f'Missing value: a={a}, b={b}')
    return a - b

def multiply(a, b):
    if a is None or b is None:
        raise ValueError(f'Missing value: a={a}, b={b}')
    return a * b

def divide(a, b):
    if a is None or b is None:
        raise ValueError(f'Missing value: a={a}, b={b}')
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
