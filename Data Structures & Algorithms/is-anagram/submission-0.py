class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        for ch in sCount:
            if sCount[ch] != tCount.get(ch, 0):
                return False

        return True

        