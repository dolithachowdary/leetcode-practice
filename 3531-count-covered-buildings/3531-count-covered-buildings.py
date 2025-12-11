from typing import List
import math
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Use dicts since coordinates can be very large (up to 1e9)
        row_min = defaultdict(lambda: math.inf)
        row_max = defaultdict(lambda: -math.inf)
        col_min = defaultdict(lambda: math.inf)
        col_max = defaultdict(lambda: -math.inf)

        # First pass: compute min/max for each row and column
        for r, c in buildings:
            row_min[r] = min(row_min[r], c)
            row_max[r] = max(row_max[r], c)
            col_min[c] = min(col_min[c], r)
            col_max[c] = max(col_max[c], r)

        # Second pass: count covered buildings
        covered = 0
        for r, c in buildings:
            if row_min[r] < c < row_max[r] and col_min[c] < r < col_max[c]:
                covered += 1

        return covered
