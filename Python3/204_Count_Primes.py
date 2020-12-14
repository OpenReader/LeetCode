class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1] * n
        i = 2
        while i*i < n:
            if primes[i] == 1:
                m = 2
                while m*i < n:
                    primes[i*m] = 0
                    m += 1
            i += 1
        # for i, p in enumerate(primes):
        #     print("%d: %d" % (i, p))
        return sum(primes) - 2