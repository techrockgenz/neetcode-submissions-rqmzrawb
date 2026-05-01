# E * log V , V^2 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for src, dest, dis in times:
            edges[src].append((dest, dis))
        
        minHeap = [(0, k)] # k is starting node
        visit = set()
        t = 0

        while minHeap:
            dis, src = heapq.heappop(minHeap)
            if src in visit:
                continue
            visit.add(src)
            t = dis

            # Till here nothing, just pop from minHeap, visit and set time
            # After this if node not visited i.e. all BFS keep on pushing, with 
            # distance from starting point i.e. dis + current distance nextDis
            for nextSrc, nextDis in edges[src]:
                if nextSrc not in visit:
                    heapq.heappush(minHeap, (dis + nextDis, nextSrc))

        return t if len(visit) == n else -1 # If connected