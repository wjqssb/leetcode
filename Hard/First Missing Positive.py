class Solution:
    """
    1. 只考虑正整数，将正整数i，放到数组下标为i-1的位置，即index=0放置1，index=1放置2
    2. 具体就是遍历一边数组，过程中将符合条件的正整数与相应位置的数字交换
    3. 最后再遍历一遍数组，得到结果
    """
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        i = 0
        while i < n and i + 1 == nums[i]:
            i += 1
        return i + 1

