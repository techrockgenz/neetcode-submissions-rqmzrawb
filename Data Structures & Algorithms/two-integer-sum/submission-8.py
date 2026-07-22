# n, n
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentsIndicesMap = {}

        for index, num in enumerate(nums):
            complimentsIndicesMap[num] = index

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in complimentsIndicesMap and complimentsIndicesMap[compliment] != index:
                return [index, complimentsIndicesMap[compliment]]        