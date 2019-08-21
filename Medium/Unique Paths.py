class Solution:
    def __init__(self):
        self.count = 0

    def uniquePaths(self, m: int, n: int) -> int:
        self.helper(m, n, 0, 0)
        return self.count

    def helper(self, m, n, x, y):
        if x == m-1 and y == n-1:
            self.count += 1
            return
        if x < m-1:
            self.helper(m, n, x+1, y)
        if y < n-1:
            self.helper(m, n, x, y+1)

s = Solution()



# 动态规划解法
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

s = Solution2()
print(s.uniquePaths(7,3))