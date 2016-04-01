from main import lisp_eval, lisp_call, unpack_expr


def test_lisp_eval():
    assert lisp_eval('(+ 1 2)') == 3


def test_lisp_eval_recursive():
    assert lisp_eval('(+ 1 (+ 2 3))') == 6


def test_lisp_call():
    assert lisp_call('+', 1, 2) == 3


def test_unpack_expr():
    assert unpack_expr('(+ 1 (+ 2 3))') == ['+', '1', '(+ 2 3)']
