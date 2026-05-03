# Brute force 2 ^ n
# n * sum(nums) / 2, n * sum(nums), since num is max 200, its good 
# Space is also same, but using DP we can reduce it
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        if target in nums:
            return True

        # for i in range(len(nums) - 1, -1, -1):
        for i in range(len(nums)):
            for t in dp.copy():
                newTarget = t + nums[i]
                if newTarget == target: return True
                dp.add(newTarget)
        return False    