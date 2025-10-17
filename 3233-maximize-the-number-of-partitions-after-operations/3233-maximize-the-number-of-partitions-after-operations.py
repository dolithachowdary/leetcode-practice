class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        from functools import lru_cache

        n = len(s)

        @lru_cache(None)
        def dfs(i: int, mask: int, changed: bool) -> int:
            # mask = bitmask of distinct letters seen in current prefix
            # changed = whether we already used the single allowed change
            if i == n:
                return 1  # last partition

            best = 0
            # Option 1: take s[i] as is
            bit = 1 << (ord(s[i]) - 97)
            new_mask = mask | bit
            if bin(new_mask).count("1") <= k:
                best = max(best, dfs(i + 1, new_mask, changed))
            else:
                best = max(best, 1 + dfs(i + 1, 1 << (ord(s[i]) - 97), changed))

            # Option 2: change s[i] (only once allowed)
            if not changed:
                for c in range(26):
                    bit2 = 1 << c
                    new_mask2 = mask | bit2
                    if bin(new_mask2).count("1") <= k:
                        best = max(best, dfs(i + 1, new_mask2, True))
                    else:
                        best = max(best, 1 + dfs(i + 1, bit2, True))

            return best

        return dfs(0, 0, False)
