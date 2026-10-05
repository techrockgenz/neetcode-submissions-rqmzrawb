class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            indices[num] = index

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in indices and indices[compliment] != index:
                return [min(indices[compliment], index),
                        max(indices[compliment], index)]
        return [-1, -1]