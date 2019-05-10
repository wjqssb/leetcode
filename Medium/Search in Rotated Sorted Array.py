class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if target == nums[mid]:
                return mid
            # 左半段为有序
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
