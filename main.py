from functools import reduce
from operator import add

from funcy import compose, partial, silent, some_fn


defined_fns = {'+': '+'}


def eval_expr(text):
    def recursive_eval(acc, char):
        items, in_parens, temp = acc

        if not in_parens:
            if char == ' ':
                return acc
            if char == '(':
                return items, True, temp + char
            return items + [lisp_eval(char)], in_parens, temp
        else:
            new_temp = temp + char
            if char == ')':
                return items + [lisp_eval(new_temp)], False, ''
            return items, in_parens, new_temp

    without_parens = text[1:-1]
    items, _, _ = reduce(recursive_eval, without_parens, ([], False, ''))
    fn, *args = items
    return lisp_call(fn, *args)


lisp_eval = some_fn(
    partial(dict.get, defined_fns),
    lambda t: silent(eval)(t),
    eval_expr)


def lisp_call(fn, *args):
    if fn == '+':
        return reduce(add, map(int, args), 0)
    else:
        raise NotImplementedError
