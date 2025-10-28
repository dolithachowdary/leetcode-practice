class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev = 0
        for row in bank:
            curr = row.count('1')
            if curr:
                beams += prev * curr
                prev = curr
        return beams
 