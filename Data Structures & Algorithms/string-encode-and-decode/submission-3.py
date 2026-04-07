class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            if i == 0:
                res = strs[i]
            else:
                res = res + "###Delim###" + strs[i]

        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        return list(s.split("###Delim###"))