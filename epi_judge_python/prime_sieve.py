from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    seive = [i for i in range(n+1)]
    primes = []
    for i in range(2, n + 1):
        if seive[i] != 0:
            primes.append(i)
            x = i
            while x <= n:
                seive[x] = 0
                x += i
    return primes


if __name__ == '__main__':
    # print(generate_primes(10))
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
