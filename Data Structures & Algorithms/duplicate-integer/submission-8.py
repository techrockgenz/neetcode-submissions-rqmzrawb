# Brute force n2, 1
# Sorting n log n, n or 1
# Hashset n, n

# len(nums) != len(set(nums))
# len(set(nums)) < len(nums)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False   