class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, top = 0, 0
        right, bottom = n, n

        curr = 1
        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = curr
                curr += 1
            top += 1

            for i in range(top, bottom):
                matrix[i][right - 1] = curr
                curr += 1
            right -= 1

            if top != bottom:
                for i in list(reversed(range(left, right))):
                    matrix[bottom - 1][i] = curr
                    curr += 1
                bottom -= 1

            if left != right:
                for i in list(reversed(range(top, bottom))):
                    matrix[i][left] = curr
                    curr += 1
                left += 1

        return matrix

    def generateMatrix_2(self, n: int):
        ans = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 0, 1
        for i in range(1, n * n + 1):
            ans[x][y] = i
            if ans[(x + dx) % n][(y + dy) % n] > 0:
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        return ans

s = Solution()
print(s.generateMatrix_2(3))
