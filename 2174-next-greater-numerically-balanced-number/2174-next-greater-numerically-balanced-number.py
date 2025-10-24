class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            # digits can't include 0 (if 0 appears, it should appear 0 times → impossible)
            cnt = [0] * 10
            y = x
            while y:
                d = y % 10
                if d == 0:
                    return False
                cnt[d] += 1
                y //= 10
            # for every digit that appears, its count must equal the digit
            for d in range(1, 10):
                if cnt[d] != 0 and cnt[d] != d:
                    return False
            return True

        m = n + 1
        # It’s known the answer is <= ~1_224_444 for n <= 1e6, but we can just loop.
        while True:
            if is_balanced(m):
                return m
            m += 1
