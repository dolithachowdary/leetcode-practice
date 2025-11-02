class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        # mark guards and walls
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        # directions: up, down, left, right
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3  # mark guarded
                    nr += dr
                    nc += dc
        
        # count unguarded cells (0)
        ans = sum(cell == 0 for row in grid for cell in row)
        return ans
