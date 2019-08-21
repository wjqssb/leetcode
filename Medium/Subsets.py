class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
            print(res)
        return res

s = Solution()
print(s.subsets([1,2,3]))