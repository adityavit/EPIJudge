from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    i = len(A) - 1
    carry = 1
    while i >= 0 and carry > 0:
        sum = A[i] + carry
        A[i] = sum % 10
        carry = sum//10
        i -= 1
    if carry > 0:
        return [1] + A[:]
    return A


if __name__ == '__main__':
    # print(plus_one([9]))
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
