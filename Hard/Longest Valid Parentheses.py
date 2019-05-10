"""
No.32 hard
"""


class Solution:
    """
    我们用 dp[i] 表示以 i 结尾的最长有效括号；

        1.当s[i] 为'(',dp[i] 必然等于0,因为不可能组成有效的括号;

        2.那么s[i] 为 ')'

            2.1 当 s[i-1] 为 '('，那么 dp[i] = dp[i-2] + 2；

            2.2 当 s[i-1] 为 ')' 并且 s[i-dp[i-1] - 1] 为 '('，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]；

    时间复杂度：O(n)
    """
    def longestValidParentheses_1(self, s: str) -> int:

        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

    '''
    找出所有括号匹配的位置，看最大连续长度
    '''
    def longestValidParentheses_2(self, s):
        # st只存放左括号的index，b用来记录匹配括号的index
        st, b = [], [0]*len(s)
        for i, val in enumerate(s):
            if val == '(':
                st.append(i)
            elif st:
                b[st.pop()], b[i] = 1, 1
        # 遍历b，计算最长连续的匹配长度
        c, mc = 0, 0
        for i in b:
            if i:
                c += 1
            else:
                mc = max(c, mc)
                c = 0

        return max(c, mc)

    def longestValidParentheses_3(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res

    def isMatch(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False




s = Solution()
print(s.isMatch("((("))