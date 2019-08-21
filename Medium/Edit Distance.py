class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for index, i in enumerate(range(len(dp))):
            dp[i][0] = index
        for index, i in enumerate(range(len(dp[0]))):
            dp[0][i] = index


        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[-1][-1]

s = Solution()
print(s.minDistance("plasma","altruism"))



