class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, top = 0, 0
        right = len(matrix[0])
        bottom = len(matrix)
        while left != right and top != bottom:
            for i in range(left, right):

                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if top != bottom:
                for i in list(reversed(range(left, right))):
                    res.append(matrix[bottom-1][i])
                bottom -= 1

            if left != right:
                for i in list(reversed(range(top, bottom))):
                    res.append(matrix[i][left])
                left += 1

        return res

s = Solution()
print(s.spiralOrder([[ 6, 7, 9 ]]))