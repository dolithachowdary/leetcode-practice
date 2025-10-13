class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ans = []
        prev_sorted = None
        for w in words:
            sw = ''.join(sorted(w))
            if sw != prev_sorted:
                ans.append(w)
                prev_sorted = sw
        return ans
