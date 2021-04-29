from calculator import calculator

def test_add_one():
    test_input = 1
    test_output = 2
    real_output = calculator.add_one(test_input)
    assert test_output == real_output

    test_input = -1
    test_output = 0
    real_output = calculator.add_one(test_input)
    assert test_output == real_output

def test_multiply_by_ten():
    test_input = 30
    test_output = 300
    real_output = calculator.multiply_by_ten(test_input)
    assert test_output == real_output