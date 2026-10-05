# Sorting n log n, n - not bester than earlier.
# Give insight of:
# i. Two pointers
# ii. Emphasis on order of answer. i.e. Order of returning indices.
#     Lowest firt and then higher
class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        sortedNums = []
        for index, num in enumerate(nums):
            sortedNums.append([num, index])
        
        sortedNums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current = sortedNums[left][0] + sortedNums[right][0]
            if current == target:
                return [min(sortedNums[left][1], sortedNums[right][1]),
                        max(sortedNums[left][1], sortedNums[right][1])]
            elif current < target:
                left += 1
            else:
                right -= 1      