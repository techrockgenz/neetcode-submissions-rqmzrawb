class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = []
        for index, num in enumerate(nums):
            map.append([num, index])

        map.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current = map[left][0] + map[right][0]
            if current == target:
                return [min(map[left][1], map[right][1]),
                        max(map[left][1], map[right][1])]
            elif current < target:
                left += 1
            else:
                right -= 1