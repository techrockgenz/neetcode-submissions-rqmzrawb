class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}':'{',
                ']':'[',
                ')':'('}
        stack = []
        for ch in s:
            if ch in pairs:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False