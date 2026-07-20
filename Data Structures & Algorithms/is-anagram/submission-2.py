# s + t, s + t
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False

        sCount, tCount = {}, {}

        # for ch in s:
        #     sCount[ch] = sCount.get(ch) + 1
        
        # for ch in t:
        #     tCount[ch] = tCount.get(ch) + 1

        for index in range(len(s)):
            sCount[s[index]] = sCount.get(s[index], 0) + 1
            tCount[t[index]] = tCount.get(t[index], 0) + 1
        
        for ch in sCount:
            if sCount[ch] != tCount.get(ch, 0):
                return False

        return True