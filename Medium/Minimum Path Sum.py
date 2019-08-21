class Solution:
    def minPathSum(self, grid):
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]

        dp[0][0] = grid[0][0]
        i = 1
        while i < len(dp[0]):
            dp[0][i] = dp[0][i-1]+grid[0][i]
            i += 1
        i = 1
        while i < len(dp):
            dp[i][0] = dp[i-1][0]+grid[i][0]
            i += 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]

s = Solution()
print(s.minPathSum([[7,4,8,7,9,3,7,5,0],
                    [1,8,2,2,7,1,4,5,7],
                    [4,6,4,7,7,4,8,2,1],
                    [1,9,6,9,8,2,9,7,2],
                    [5,5,7,5,8,7,9,1,4],
                    [0,7,9,9,1,5,3,9,4]]))