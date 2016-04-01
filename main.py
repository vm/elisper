from functools import reduce
from operator import add

from funcy import compose, partial, silent, some_fn


defined_fns = {'+': '+'}


def eval_expr(text):
    without_parens = text[1:-1]

    items = []
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
                items.append(lisp_eval(char))
        else:
            temp += char
            if char == ')':
                in_parens = False
                items.append(lisp_eval(temp))
                temp = ''

    return lisp_call(*items)


lisp_eval = some_fn(
    partial(dict.get, defined_fns),
    lambda t: silent(eval)(t),
    eval_expr)



def lisp_call(fn, *args):
    if fn == '+':
        return reduce(add, map(int, args), 0)
    else:
        raise NotImplementedError
