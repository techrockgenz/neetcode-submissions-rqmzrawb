
# n log n

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heapq.heappush(stones, -abs(heapq.heappop(stones) - heapq.heappop(stones)))

        stones.append(0) # Edge case if stone is empty, works even if not
        return abs(stones[0])
