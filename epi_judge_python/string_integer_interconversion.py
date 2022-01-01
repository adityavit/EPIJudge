from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    if x == 0:
        return "0"
    neg = ""
    if x < 0:
        neg = "-"
        x = -1 * x
    sol = []
    while x > 0:
        sol.append(chr(ord('0') + x % 10))
        x = x//10
    return neg + "".join(reversed(sol))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    if len(s) == 0:
        return 0
    neg = 1
    if s[0] == '+':
        s = s[1:]
    if s[0] == '-':
        neg = -1
        s = s[1:]
    i, num = 0, 0
    while i < len(s):
        num = num * 10 + (ord(s[i]) - ord('0'))
        i += 1
    return neg * num


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    # s = int_to_string(-123)
    # print(s)
    # n = string_to_int(s)
    # print(n)
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
