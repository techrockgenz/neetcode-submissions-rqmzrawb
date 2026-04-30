class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            soFar = 1
            soFar += dfs(r - 1, c)
            soFar += dfs(r + 1, c)
            soFar += dfs(r, c - 1)
            soFar += dfs(r, c + 1)
            return soFar

        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r, c), res)
        return res