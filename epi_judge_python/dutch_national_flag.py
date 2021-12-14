import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pi: int, A: List[int]) -> None:
    # TODO - you fill in here.
    p = A[pi]
    s, e, h = 0, 0, 0
    while h < len(A):
        if A[h] < p:
            swap(A, e, h)
            swap(A, s, e)
            h += 1
            s += 1
            e += 1
        elif A[h] == p:
            swap(A, e, h)
            e += 1
            h += 1
        else:
            h += 1
    return

def swap(A: List[int], i, j: int):
    A[i], A[j] = A[j], A[i]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    # A = [0,1,2,3,2,1,1]
    # dutch_flag_partition(2, A)
    # print(A)
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
