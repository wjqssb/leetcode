class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return []
        nums = [i + 1 for i in range(n)]
        used = [False for _ in range(n)]

        return self.__dfs(nums,n,k,0,[],used)

    def __factorial(self, n):
        # 这种编码方式包括了 0 的阶乘是 1 这种情况
        res = 1
        while n:
            res *= n
            n -= 1
        return res

    def __dfs(self, nums, n, k, depth, pre, used):
        if depth == n:
            return ''.join(pre)

        ps = self.__factorial(n-depth-1)
        for i in range(n):
            if used[i]:
                continue
            if ps<k:
                k -= ps
                continue
            pre.append(str(nums[i]))
            used[i] = True
            return self.__dfs(nums,n,k,depth+1,pre,used)


s = Solution()

print(s.getPermutation(4,9))