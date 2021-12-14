from typing import List

from test_framework import generic_test

base = 10
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    if (len(num1) == 1 and num1[0] == 0) or (len(num2) == 1 and num2[0] == 0):
        return [0]
    neg = 1
    if num1[0] * num2[0] < 0:
        neg = -1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    res = [0]
    for j in reversed(range(len(num2))):
        k = len(num2) - 1 - j
        for i in reversed(range(len(num1))):
            mul = num1[i] * num2[j]
            if k > len(res) - 1:
                res.append(0)
            res[k] += mul
            carry = res[k] // 10
            res[k] = res[k] % 10
            if carry > 0:
                if k + 1 > len(res) - 1:
                    res.append(0)
                res[k+1] += carry
            k += 1
    res.reverse()
    res[0] = res[0] * neg
    return res

if __name__ == '__main__':
    # print(multiply([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]))
    # print(multiply([1, 9], [1, 1, 1]))
    # num1 = [-4, 7, 5, 8, 9, 6, 9, 5, 1, 9, 2, 8, 0, 3, 0, 9, 0, 0, 1, 1, 6, 1, 9, 2, 3, 6, 9, 2, 4, 0, 9, 0, 2, 7, 3, 2,
    #        0, 5, 9, 5, 0, 0, 2, 7, 5, 1, 1, 2, 4, 6, 3, 2, 6, 8, 6, 2, 8, 3, 6, 4, 5, 2, 4, 1, 9, 8, 5, 5, 8, 9, 2, 3,
    #        3, 7, 6, 5, 6]
    # num2 = [-5, 4, 0, 1, 7, 3, 5, 3, 7, 3, 8, 9, 3, 1, 9, 3, 3, 5, 8, 0, 5, 6, 9, 5, 5, 5, 1, 0, 4, 2, 2, 8, 2, 6, 0, 6,
    #        7, 6, 7, 4, 7, 4, 5, 4, 4, 6, 8, 7, 6, 4, 9, 1, 3, 2, 5, 1, 0, 4, 6, 5, 9, 8, 4, 5, 4, 3, 4, 0, 7, 7, 1, 3,
    #        0, 6, 2, 6, 5, 7, 5, 9, 6, 6, 4, 5, 9, 9, 3, 1, 3, 4, 0, 6]
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
