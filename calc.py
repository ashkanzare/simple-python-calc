from exceptions import DivisionByZeroError, InvalidOperatorException


def calculator(x, y, operator):
    # check operator
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '**':
        return x ** y
    elif operator == '%':
        return x * y / 100
    elif operator == '/':
        try:
            return x / y
        except ZeroDivisionError:
            raise DivisionByZeroError
    else:
        raise InvalidOperatorException

