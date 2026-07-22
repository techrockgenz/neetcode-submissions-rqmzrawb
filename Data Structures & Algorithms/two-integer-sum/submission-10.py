# n, n, one pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementIndexMap = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in complementIndexMap:
                return [complementIndexMap[complement], index]
            complementIndexMap[num] = index 

# Note: Return values are indices and not the actual values