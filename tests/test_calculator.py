from app import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_divide_by_zero():
    try:
        calculator.divide(1, 0)
    except ValueError:
        assert True
    else:
        assert False
