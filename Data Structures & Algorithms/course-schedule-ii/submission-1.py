# Topological Sort
# E + V

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # a course has 3 possible states:

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to visiting
        # unvisited -> crs not added to output or visiting

        visiting = set()
        output = []

        def dfs(crs):
            if crs in visiting:
                return False # Cycle
            if crs in output:
                return True
            visiting.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False # Cycle
            visiting.remove(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return [] # Cycle
        return output


        