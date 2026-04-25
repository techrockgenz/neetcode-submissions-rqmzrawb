# 5 9 13 1 2 3
# 1 2 3 5 9 13
# 2 3 5 9 13 1
# 9 1 2 3 5 6

# Can't compare l > m, it'll work for few but not for others

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]