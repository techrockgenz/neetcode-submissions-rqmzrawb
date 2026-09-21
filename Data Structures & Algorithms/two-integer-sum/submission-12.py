# Don't add all elements first, same number reuse is not allowed
# [2, 1, 4, 3] target 4.
# 2 in array, then while checking it 2 + 2 = 4, wrong

# n2, 1 Brute force
# n, n

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        prevMap = {} # val : index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index

        # Answer is guarantted so, no return in end