# Brute force 2 ^ n
# n * sum(nums) / 2, n * sum(nums), since num is max 200, its good 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set(dp.copy())
            for t in dp:
                newTarget = t + nums[i]
                # if newTarget: return True
                nextDP.add(newTarget)
            dp = nextDP
        return True if target in dp else False    