class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1): # skip last, as we are comparing next
        # but this will anyways be skip in next line
        # e.g. 0 - 6 for 7 elements. i = 6, j = 7, 6 will not go in loop.
        # with - 1, i = 0 - 5 and j = 1 - 6.
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []