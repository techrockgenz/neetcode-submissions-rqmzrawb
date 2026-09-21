# Hashmap n + m, n + m
# Sort n log n, 1 or n
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)

        # return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # for index in range(len(s)):
        #     countS[s[index]] = 1 + countS.get(s[index], 0)
        #     countT[t[index]] = 1 + countT.get(t[index], 0)
    
        for index, ch in enumerate(s):
            countS[ch] = 1 + countS.get(ch, 0)
            countT[t[index]] = 1 + countT.get(t[index], 0)
        
        for ch in countS:
            if countS[ch] != countT.get(ch, 0):
                return False
        return True