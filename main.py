import re
from parse import parse_final, parse
from calc import calculator
import sys

# sys.tracebacklimit = 0


def calc(text):
    if '(' in text:
        temp = str(parse(text, '(')[-1])
        text = text.replace(f"({temp})", str(calc(temp)))
        return calc(text)

    elif 'e+' in text and text.count('+') == 1 and re.search("[-*/+]", text):
        if re.search("[-*/+]", text).group() == '+':
            return text
        temp = parse_final(text)
        return calculator(temp[0], temp[1], temp[2])

    elif '+-' in text:
        text = text.replace('+-', '-')
        return calc(text)

    elif '--' in text:
        text = text.replace('--', '+')
        return calc(text)

    elif '-+' in text:
        text = text.replace('-+', '-')
        return calc(text)

    elif '/-' in text:
        temp1 = parse(text, '/-')
        temp3 = temp1[0]
        temp1 = temp1[-1]
        temp2 = parse_final(temp1)
        text = text.replace(f"{temp3}", str(calculator(temp2[0], temp2[1], temp2[2])))
        return calc(text)

    elif '*-' in text:
        temp1 = parse(text, '*-')
        temp3 = temp1[0]
        temp1 = temp1[-1]
        temp2 = parse_final(temp1)
        text = text.replace(f"{temp3}", str(calculator(temp2[0], temp2[1], temp2[2])))
        return calc(text)

    elif '*' in text:
        temp1 = parse(text, '*')[-1]
        temp2 = parse_final(temp1)
        text = text.replace(f"{temp1}", str(calculator(temp2[0], temp2[1], temp2[2])))
        return calc(text)

    elif '/' in text:
        temp1 = parse(text, '/')[-1]
        temp2 = parse_final(temp1)
        text = text.replace(f"{temp1}", str(calculator(temp2[0], temp2[1], temp2[2])))
        return calc(text)

    elif '+' in text:
        temp1 = parse(text, '+')[-1]
        temp2 = parse_final(temp1)
        text = text.replace(f"{temp1}", str(calculator(temp2[0], temp2[1], temp2[2])))
        return calc(text)

    elif '-' in text:
        if text[0] == '-':
            return text
        temp1 = parse(text, '-')[-1]
        temp2 = parse_final(temp1)
        text = text.replace(f"{temp1}", str(calculator(temp2[0], temp2[1], temp2[2])))
        return calc(text)

    return text
