# 2 ^ n top-down, brute force
# n, top-down, memoization

# n, n, bottom-up, Tabulation

class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1

        for i in range(n - 1):
            one, two = one + two, one
        return one