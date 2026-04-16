class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        res = 0
        maxF = 0
        for right in range(len(s)):
            rChar = s[right]
            counter[rChar] = 1 + counter.get(rChar, 0)
            currentLength = right - left + 1
            maxF = max(maxF, counter[rChar])
            while currentLength - maxF > k:
                counter[s[left]] -= 1
                left += 1
                currentLength = right - left + 1
            res = max(res, currentLength)
        return res