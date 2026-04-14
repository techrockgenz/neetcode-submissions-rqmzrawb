class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in subSet:
                subSet.remove(s[left])
                left += 1
            subSet.add(s[right])
            res = max(res, len(subSet))

        return res