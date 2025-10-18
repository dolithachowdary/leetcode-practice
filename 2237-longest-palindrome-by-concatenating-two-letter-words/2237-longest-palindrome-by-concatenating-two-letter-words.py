class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        freq = {}
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

        length = 0
        center = False

        for w in list(freq.keys()):
            rev = w[::-1]
            if w == rev:
                # same letters like "aa", "bb"
                pairs = freq[w] // 2
                length += pairs * 4
                freq[w] -= pairs * 2
                if freq[w] > 0:
                    center = True
            elif rev in freq:
                # use pairs between w and its reverse
                pairs = min(freq[w], freq[rev])
                length += pairs * 4
                freq[w] -= pairs
                freq[rev] -= pairs

        if center:
            length += 2

        return length
