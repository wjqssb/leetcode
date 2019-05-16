class Solution:
    '''
    递归法，超时
    '''
    def isMatch(self, s: str, p: str) -> bool:
        if s and not p:
            return False
        if not s and not p:
            return True
        if not s and p:
            for i in p:
                if i != '*':
                    return False
            return True
        if p[0] != '*':
            if s[0] != p[0] and p[0] != '?':
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)

    '''
    动态规划：
    
    初始化
    dp[0][0] = True
    dp[0][j] = True if p[j] = '*' and dp[0][j-1]
    dp[i][0] = False

    状态转移  
    dp[i][j] = True 
    1. if s[i] = p[j] or p[j] == '?' and dp[i-1][j-1]
    2. if p[j] == '*' and (dp[i-1][j] or dp[i][j-1])

    '''

    def isMatch_2(self, s: str, p: str) -> bool:

        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        for j in range(1, len(p) + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))