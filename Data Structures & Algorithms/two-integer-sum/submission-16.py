# Don't add all elements first, same number reuse is not allowed
# [2, 1, 4, 3] target 4.
# 2 in array, then while checking it 2 + 2 = 4, wrong

# Brute force n2, 1
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
'''
# A two pass solution as well, but better is above, i.e. one pass
# n, n - Same as above
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # val : index
        for index, num in enumerate(nums):
            indices = index
        
        for index, num in enumerate(nums):
            diff = target - n
            if diff in indiecs and indices[diff] != index:
                return [index, indices[diff]]
            # Note condition after and, not to repeat same
            # Why indices[diff], diff is value and map is value:index
            # Not index:value
'''