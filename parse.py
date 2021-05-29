import re
from exceptions import InvalidFormatException, InvalidNumberException
from calc import calculator
import string

def is_float(text_input, punc):
    try:
        if text_input[0] == '-' and text_input.count('-') == 1 and punc == '+':
            return True

        if text_input[0] in ['+']:
            return False

        float(text_input)
        return True
    except (ValueError, IndexError):
        return False


def parse(x, punc):

    check = ''
    if punc == '(':
        return True, re.search('\(([0-9]*|[0-9]*\.[0-9]*)[\+\-\/\*]([0-9]*|[0-9]*\.[0-9]*)\)', x).group()[1:-1]
    if punc in x:
        if punc == '*-':
            x = x.replace('*-', '*')
            punc = '*'
            check = '-'

        if punc == '/-':
            x = x.replace('/-', '/')
            punc = '/'
            check = '-'
        if x[0] == '-' and punc == '-':
            punc_ind = x[1:].index(punc) + 1
            front = x[punc_ind + 1:]
            back = x[:punc_ind]
        else:

            punc_ind = x.index(punc)
            front = x[punc_ind + 1:]
            back = x[:punc_ind]
        dic = {(0, -1): front, (1, len(back)): back}
        values = []
        lens = []
        if front == '' or back == '':
            raise InvalidFormatException
        for pair in dic:
            if is_float(dic[pair], punc):
                values.append(float(dic[pair]))
                lens.append(len(dic[pair]))
                continue

            while not is_float(dic[pair], punc):
                if re.search(f'[{string.ascii_letters}]', dic[pair]):
                    raise InvalidNumberException
                dic[pair] = dic[pair][pair[0]:pair[1]]


            values.append(float(dic[pair]))
            lens.append(len(dic[pair]))


        return x[punc_ind - lens[-1]: punc_ind] + punc+ '-' + x[punc_ind + 1:punc_ind + lens[0] + 1], values, \
               check + x[punc_ind - lens[-1]:punc_ind + lens[0] + 1]


def parse_final(text):
    try:

        punc = re.search('([0-9]|[\.])[\+\*\/\-\**\%]([0-9]|[\.])', text).start() + 1
        punc_format = text[punc]


    except AttributeError:
        raise InvalidFormatException
    else:
        if 'e+' in text:
            text = text.replace('e+', 'E')

        if 'e-' in text:
            text = text.replace('e-', 'E')
        if text[0] == '-' and text[punc] == '-':
            list_ = list(text)
            list_[0] = '#'
            text = ''.join(list_)

        text = text.split(text[punc])

        if text[0][0] == '#':
            list_ = list(text[0])
            list_[0] = '-'

            text[0] = ''.join(list_)



        for i in range(len(text)):
            if 'E' in text[i]:
                text[i] = text[i].replace('E', 'e+')
        if len(text) == 2:
            x = text[0]
            operator = punc_format
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

