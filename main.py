from funcy import partial, silent, some_fn


"""
A Token is one of:
    - String
    - Integer
    - ['+' Token Token]
"""


def parse_recursive(sexp):
    first, last = sexp[0], sexp[-1]

    if first != '(' or last != ')' or len(sexp) < 2:
        raise TypeError('not a valid function call')

    middle = sexp[1:-1]

    sexps = []
    depth = 0
    temp = ''
    for char in middle:
        if depth == 0:
            if char != ' ':
                temp += char
                if char == '(':
                    depth += 1
            else:
                sexps.append(temp)
                temp = ''
        else:
            temp += char
            if char == ')':
                depth -= 1
    if temp:
        sexps.append(temp)

    return list(map(parse_sexp, sexps))


def parse_string(sexp):
    quote = '"'
    print(quote)
    if sexp[0] == quote and sexp[-1] == quote:
        return sexp[1:-1]
    return None


parse_var = partial(dict.get, {'+': '+'})
parse_integer = silent(int)


parse_sexp = some_fn(parse_var, parse_string, parse_integer, parse_recursive)
