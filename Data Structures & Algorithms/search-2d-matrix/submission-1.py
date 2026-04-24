class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = top + ((bottom - top) // 2)
            if (matrix[row][0] == target or
                matrix[row][len(matrix[row]) - 1] == target):
                return True
            elif matrix[row][-1] < target: # Note: -1
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        # Imp:
        if not (top <= bottom):
            return False
        
        row = top + ((bottom - top) // 2)
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

