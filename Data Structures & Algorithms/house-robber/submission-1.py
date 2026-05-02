# n, 1
class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = house2 = 0

        # [house1, house2, money1, money2, .....]
        for money in nums:
            maxMoney = max(money + house1, house2)
            house1 = house2
            house2 = maxMoney
        return house2