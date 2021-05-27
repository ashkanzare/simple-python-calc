# father class of calc errors
class CalcError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None


# child class of CalcError that catch error if inputs are not numbers
class InvalidNumberException(CalcError):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        if self.message:
            return f'InvalidNumberException, {self.message}'
        else:
            return 'Inputs must be integer or float.\n'


# child class of CalcError that catch error if operator is not valid
class InvalidOperatorException(CalcError):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        if self.message:
            return f'InvalidOperatorException, {self.message}'
        else:
            return 'Operator must be + - * / ** %\n'


# child class of CalcError that catch error if number divided by 0
class DivisionByZeroError(CalcError):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        if self.message:
            return f'DivisionByZeroError, {self.message}'
        else:
            return 'Second input must be non-zero\n'


# child class of CalcError that catch error if input format is not valid
class InvalidFormatException(CalcError):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        if self.message:
            return f'InvalidFormatException, {self.message}'
        else:
            return 'Input format must be like:\n Input1<whitespace>Operator<whitespace>Input2\n ' \
                   'example:  2 + 13 \n'
