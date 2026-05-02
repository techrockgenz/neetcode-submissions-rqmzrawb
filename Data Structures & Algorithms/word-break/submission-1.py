class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): # Reverse order
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)] # Crux dp[0] = dp[0 + len("leet")] =  0 + 4 = dp[4] = True
                                           # As we already calculated from reverse 
                    if dp[i]: # If found one word break inner loop
                        break
        return dp[0]