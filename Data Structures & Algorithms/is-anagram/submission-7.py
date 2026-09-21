# Hashmap n + m, n + m
# Sort n log n, 1 or n
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for index in range(len(s)):
            countS[s[index]] = 1 + countS.get(s[index], 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True