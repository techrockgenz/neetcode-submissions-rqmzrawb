class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "###NULL###"
        res = ""
        for i in range(len(strs)):
            if i == 0:
                res = strs[i]
            else:
                res = res + "###Delim###" + strs[i]

        return res

    def decode(self, s: str) -> List[str]:
        if s == "###NULL###":
            return []
        if s == "":
            return [""]
        return list(s.split("###Delim###"))