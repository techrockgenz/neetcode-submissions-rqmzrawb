class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            index1 = left + ((right - left) // 2)
            index2 = half - index1 - 2

            Aleft = A[index1] if index1 >= 0 else float("-inf")
            Aright = A[index1 + 1] if (index1 + 1) < len(A) else float("inf")
            Bleft = B[index2] if index2 >= 0 else float("-inf")
            Bright = B[index2 + 1] if (index2 + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = index1 - 1
            else:
                left = index1 + 1