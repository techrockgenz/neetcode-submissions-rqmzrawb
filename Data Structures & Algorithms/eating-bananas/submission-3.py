class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            minEat = left + ((right - left) // 2)
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/minEat)
            if totalTime <= h: # Can't optimize it to have == separte, read below
                result = minEat
                right = minEat - 1
            else:
                left = minEat + 1

        return result

# totalTime could be sitll higher even if less than h for other given lesser k