class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        start = 0
        end = len(matrix)*len(matrix[0])-1
        while start <= end:
            mid = (start+end)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid-1
            else:
                start = mid+1
        return False