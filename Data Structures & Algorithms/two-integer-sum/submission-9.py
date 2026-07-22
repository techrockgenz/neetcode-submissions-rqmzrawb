# n, n, one pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentIndexMap = {}

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in complimentIndexMap:
                return [complimentIndexMap[compliment], index]
            complimentIndexMap[num] = index