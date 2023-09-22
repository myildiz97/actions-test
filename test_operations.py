import pytest

from math_operations import add, subtract, multiply, divide

# Define test cases for the 'add' function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert round(add(0.1, 0.2), 2) == 0.3
    assert round(add(-0.1, -0.1), 2) == -0.2

def test_add_missing_value():
    with pytest.raises(ValueError) as excinfo:
        add(2, None)
    assert str(excinfo.value) == "Missing value: a=2, b=None"
    with pytest.raises(ValueError) as excinfo:
        add(None, 3)
    assert str(excinfo.value) == "Missing value: a=None, b=3"

# Define test cases for the 'subtract' function
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, -1) == 2
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
    assert round(subtract(0.1, 0.2), 2) == -0.1
    assert round(subtract(-0.1, -0.1), 2) == 0
    assert round(subtract(0.2, 0.1), 2) == 0.1

def test_subtract_missing_value():
    with pytest.raises(ValueError) as excinfo:
        subtract(None, 3)
    assert str(excinfo.value) == "Missing value: a=None, b=3"
    with pytest.raises(ValueError) as excinfo:
        subtract(2, None)
    assert str(excinfo.value) == "Missing value: a=2, b=None"

# Define test cases for the 'multiply' function
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 0) == 0
    assert round(multiply(0.1, 0.2), 2) == 0.02
    assert round(multiply(-0.1, -0.1), 2) == 0.01
    assert round(multiply(0.1, -0.1), 2) == -0.01
    assert round(multiply(-0.1, 0.1), 2) == -0.01
    assert multiply(0, 5) == 0

def test_multiply_missing_value():
    with pytest.raises(ValueError) as excinfo:
        multiply(2, None)
    assert str(excinfo.value) == "Missing value: a=2, b=None"
    with pytest.raises(ValueError) as excinfo:
        multiply(None, 3)
    assert str(excinfo.value) == "Missing value: a=None, b=3"

# Define test cases for the 'divide' function
def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(10, 2) == 5
    assert divide(0, 1) == 0
    assert round(divide(0.1, 0.2), 2) == 0.5
    assert round(divide(-0.1, -0.1), 2) == 1
    assert round(divide(0.1, -0.1), 2) == -1
    assert round(divide(-0.1, 0.1), 2) == -1

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(2, 0)
    assert str(excinfo.value) == "Cannot divide by zero"

def test_divide_missing_value():
    with pytest.raises(ValueError) as excinfo:
        divide(None, 3)
    assert str(excinfo.value) == "Missing value: a=None, b=3"
    with pytest.raises(ValueError) as excinfo:
        divide(2, None)
    assert str(excinfo.value) == "Missing value: a=2, b=None"

# Run the tests
if __name__ == '__main__':
    pytest.main()
