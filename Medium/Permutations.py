class Solution:
    def __init__(self):
        self.l = []

    def permute(self, nums):
        n = len(nums)
        self.helper(0, nums, n)
        return self.l

    def helper(self, index, nums, n):
        if index == n-1:
            self.l.append(nums.copy())
            return

        for i in range(index, n):
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp
            self.helper(index + 1, nums, n)
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp

s = Solution()
print(s.permute([1,2,3,4,5,6,7,8,9,10]))

1011123456789
9876543210111