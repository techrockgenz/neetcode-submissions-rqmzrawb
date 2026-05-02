# n^2 log n
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        
        visit.add((0, 0))

        def dfs(t, r, c):
            if (r < 0 or c < 0 or 
                r >= N or c >= N or 
                (r, c) in visit):
                return
            visit.add((r, c))
            heapq.heappush(minH, [max(t, grid[r][c]), r, c])

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            # dfs(t, r - 1, c)
            # dfs(t, r + 1, c)
            # dfs(t, r, c - 1)
            # dfs(t, r, c + 1)
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(t, r + dr, c + dc)
