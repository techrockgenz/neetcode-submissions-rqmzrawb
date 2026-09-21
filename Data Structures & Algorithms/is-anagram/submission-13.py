# n + m, 1 because at the most 26 chars
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        aOrd = ord('a')
        count = [0] * 26
        for index in range(len(s)):
            count[ord(s[index]) - aOrd] += 1
            count[ord(t[index]) - aOrd] -= 1

        for val in count:
            if val != 0:
                return False
        return True
        