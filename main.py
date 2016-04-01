from functools import reduce
from operator import add


def lisp_eval(text):
    try:
        return eval(text)
    except SyntaxError:
        fn, *args = unpack_expr(text)
        return lisp_call(fn, *map(lisp_eval, args))


def lisp_call(fn, *args):
    if fn == '+':
        return reduce(add, map(int, args), 0)
    else:
        raise NotImplementedError


def unpack_expr(text):
    without_parens = text[1:-1]

    groups = []
    temp = ''
    in_parens = False

    for char in without_parens:
        if not in_parens:
            if char == ' ':
                continue
            if char == '(':
                temp += char
                in_parens = True
            else:
                groups.append(char)
        else:
            temp += char
            if char == ')':
                in_parens = False
                groups.append(temp)
                temp = ''

    return groups
