class Solution:
    def pacificAtlantic(self, heights):
        if not heights: 
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= m or c >= n or 
                heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # Pacific (top row, left col)
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
        
        # Atlantic (bottom row, right col)
        for i in range(m):
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):
            dfs(m-1, j, atlantic, heights[m-1][j])
        
        # Intersection
        return list(pacific & atlantic)
