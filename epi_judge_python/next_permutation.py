from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    n = len(perm)
    for i in range(n - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            k = n - 1
            while k > i and perm[k] <= perm[i]:
                k -= 1
            perm[i], perm[k] = perm[k], perm[i]
            return perm[:i+1] + list(reversed(perm[i+1:]))
    return []


if __name__ == '__main__':
    # print(next_permutation([3, 2, 5, 4, 1]))
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
