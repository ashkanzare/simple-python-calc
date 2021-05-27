import re
from exceptions import InvalidFormatException, InvalidNumberException


def is_float(text_input):
    try:
        if text_input[0] in ['+', '-']:
            return False
        float(text_input)
        return True
    except (ValueError, IndexError):
        return False


def parse(x, punc):
    check = ''
    if punc == '(':
        return True, re.search('\(.+\)', x).group()[1:-1]
    if punc in x:
        if punc == '*-':
            x = x.replace('*-', '*')
            punc = '*'
            check = '-'
        punc_ind = x.index(punc)
        front = x[x.index(punc) + 1:]
        back = x[:x.index(punc)]
        dic = {(0, -1): front, (1, len(back)): back}
        values = []
        lens = []

        for pair in dic:
            if is_float(dic[pair]):
                values.append(float(dic[pair]))
                lens.append(len(dic[pair]))
                continue

            while not is_float(dic[pair]):
                dic[pair] = dic[pair][pair[0]:pair[1]]

            values.append(float(dic[pair]))
            lens.append(len(dic[pair]))

        return x[punc_ind - lens[-1]: punc_ind] + '*-' + x[punc_ind + 1:punc_ind + lens[0] + 1], values, \
               check + x[punc_ind - lens[-1]:punc_ind + lens[0] + 1]


def parse_final(text):
    try:
        punc = re.search('[0-9][\+\*\/\-\**\%][0-9]', text).group()[1]
    except AttributeError:
        raise InvalidFormatException
    else:
        if 'e+' in text:
            text = text.replace('e+', 'E')

        if 'e-' in text:
            text = text.replace('e-', 'E')

        text = text.split(punc)
        for i in range(len(text)):
            if 'E' in text[i]:
                text[i] = text[i].replace('E', 'e+')
        if len(text) == 2:
            x = text[0]
            operator = punc
            y = text[1]
            try:
                # check input text for be int or float
                x = float(x)
                y = float(y)
                return x, y, operator

            except ValueError:
                raise InvalidNumberException
        else:
            raise InvalidFormatException
