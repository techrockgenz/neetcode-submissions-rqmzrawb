class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for currentIndex, currentHeight in enumerate(heights):
            start = currentIndex
            while stack and stack[-1][1] > currentHeight:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (currentIndex - index))
                start = index
            stack. append((start, currentHeight))
        
        for index, height in stack:
            maxArea = max(maxArea, height *(len(heights) - index))
        return maxArea