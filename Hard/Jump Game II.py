import sys
class Solution:
    '''
    动态规划
    '''
    def jump(self, nums) -> int:

        maxn = nums[0]
        for i in range(1, len(nums)):
            maxn = max(maxn, nums[i])

        dp = [0]
        for i in range(1, len(nums)):
            min_step = sys.maxsize
            for j in range(max(0, i - maxn), i):
                if nums[j] >= i - j:
                    min_step = min(min_step, dp[j])
            dp.append(min_step + 1)

        return dp[-1]

    '''
    贪心算法
    '''
    def jump_2(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [0] * n
        for i in range(n):
            for j in range(nums[i], 0, -1):
                if i + j >= n - 1:

                    return dp[i] + 1
                elif dp[i + j] == 0:
                    dp[i + j] = dp[i] + 1
                else:
                    break
        return "到不了最后"

s = Solution()
print(s.jump([1,1,1,1,1,1,1,1,1,1,1]))