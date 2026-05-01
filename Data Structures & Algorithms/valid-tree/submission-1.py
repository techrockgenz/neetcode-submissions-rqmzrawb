# E + V, E + V

# No cycle
# All are connected => n == len(visited)
# Empty graph is a valid tree

# False positive for visited, so send parent/previous
# Can't consider visited, as it can have other valid cycle

# Every edge will be single 1, 0, then there will not be 0, 1
# So no cycle between two nodes

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei != par and not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n