# Sorting m * log n
# HashMap m * n
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {} # mapping charCoutn to list of Anagrams
        # Check reason below
        res = defaultdict(list) # mapping charCoutn to list of Anagrams

        for s in strs:
            count = [0] * 26 # a - z

            for ch in s:
                count[ord(ch) - ord('a')] += 1
                # res[count].append(s)
                # Can throw exception if not initialized
                # So res = defaultdict(list) in the begining
                # This avoid edge case
            res[tuple(count)].append(s)
        
        return list(res.values())