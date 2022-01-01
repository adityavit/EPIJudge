from test_framework import generic_test
from string import hexdigits

def convert_base(num: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    if num == "0":
        return "0"
    neg = ''
    if num[0] == '-':
        neg = '-'
        num = num[1:]
    n = convert_from_base(num, b1)
    return neg + convert_to_base(n, b2)

def convert_from_base(num: str, base: int) -> int:
    i, n = 0, 0
    while i < len(num):
        d = hexdigits.index(num[i].lower())
        n = n * base + d
        i += 1
    return n

def convert_to_base(num: int, base: int) -> str:
    s = []
    while num > 0:
        d = num % base
        s.append(hexdigits[d].upper())
        num = num // base
    return "".join(reversed(s))


# def baseInt(c: str) -> int:
#     return hexdigits.index(c.lower())
    # if not (ord('0') <= ord(c) <= ord('9') or ord('A') <= ord(c) <= ord('F')):
    #     return -1
    # if 0 <= ord(c) - ord('0') <= 9:
    #     return ord(c) - ord('0')
    # i = (ord(c) - ord('A')) + 10
    # if i > base:
    #     return -1
    # return i


# def baseStr(d: int) -> str:
#     if d < 10:
#         return chr(ord('0') + d)
#     return chr(ord('A') + (d - 10))

if __name__ == '__main__':
    # print(convert_base("123", 10, 2))
    # print(convert_base("1111011", 2, 10))
    # print(convert_base("615", 7, 13))
    # print(convert_base("1A7", 13, 10))
    st = []
    for i in range(10):
        st.append(i)

    for i in range(10):
        top = st.pop()
        print(top)
    # exit(
    #     generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
    #                                    convert_base))
