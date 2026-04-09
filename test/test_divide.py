def divide(a, b):
    return a / b


def test_divide():
    assert divide(1, 2) == 0.5


def do_something(condition):
    if condition:
        return 1
    else:
        return 2


def test_do_something():
    assert do_something(True) == 1
    assert do_something(False) == 2
