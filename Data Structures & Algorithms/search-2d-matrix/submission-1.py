class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif target > val:
                l = mid + 1
            else:
                r = mid - 1

        return False

            