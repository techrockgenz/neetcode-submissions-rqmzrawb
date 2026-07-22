# m * n log n, m * n
# m is number of strings and n is lenght of longest string
# note space is m * n, for sorting m strings of n length max
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            result[''.join(sorted(string))].append(string)
        
        return list(result.values())