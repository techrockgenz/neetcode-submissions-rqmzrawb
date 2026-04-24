class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            minEat = left + ((right - left) // 2)
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/minEat)
            if totalTime <= h:
                result = minEat
                right = minEat - 1
            else:
                left = minEat + 1

        return result
