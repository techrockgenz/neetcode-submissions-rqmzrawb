class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robber(nums[1:]), self.robber(nums[:-1]))

    def robber(self, nums):
        house1 = house2 = 0

        # [house1, house2, money1, money2, .....]
        for money in nums:
            maxMoney = max(money + house1, house2)
            house1 = house2
            house2 = maxMoney
        return house2