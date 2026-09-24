# m * n log n, m * n
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(List)
        res = defaultdict(list)
        # List from typing isn't an empty-list ctr, so can't be use like List()
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return [v for v in res.values()]