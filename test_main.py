from main import parse_recursive, parse_string, parse_integer, parse_var


def test_parse_recursive():
    assert parse_recursive('(+ 1 2)') == ['+', 1, 2]
    assert parse_recursive('(+ 1 (+ (+ 2 1) 3))') == ['+', 1, ['+', ['+', 2, 1], 3]]


def test_parse_string():
    assert parse_string('"hello"') == 'hello'
    assert parse_string('"9"') == '9'
    assert parse_string('9') is None


def test_parse_integer():
    assert parse_integer('100') == 100
    assert parse_integer('9') == 9
    assert parse_integer('9.') is None


def test_parse_var():
    assert parse_var('+') == '+'
    assert parse_var('#') is None
