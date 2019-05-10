class Solution:
    def searchRange(self, nums, target: int):
        res = []
        res.append(self.helper_left(nums, target))
        res.append(self.helper_right(nums, target))
        return res

    def helper_left(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) >> 1
            if target == nums[mid]:
                while mid > 0 and nums[mid - 1] == target:
                    mid -= 1
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def helper_right(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) >> 1
            if target == nums[mid]:
                while mid < len(nums) - 1 and nums[mid + 1] == target:
                    mid += 1
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

