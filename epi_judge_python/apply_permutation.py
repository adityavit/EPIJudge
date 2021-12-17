from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    for i in range(len(A)):
        c = i
        v = A[i]
        while perm[c] >= 0:
            idx = perm[c]
            A[idx], v = v, A[idx]
            perm[c] = -1
            c = idx
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
