# (V + E) ^ 2, E

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()  # Lexical order
        adj = {src:[] for src, dest in tickets}
        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1: # Done travelling all dests
                return True
            if src not in adj:  # No path to return
                return False
            
            temp = list(adj[src]) # Create a copy, as we are modifying
            for i, v in enumerate(temp):
                adj[src].pop(i)        # Try this path
                res.append(v)
                if dfs(v): return True # If successful, well and good
                adj[src].insert(i, v)  # Else backtrack
                res.pop()              # Hence pop from result 
            return False               # No path to return 

        dfs("JFK")
        return res     