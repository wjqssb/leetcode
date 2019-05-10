class Solution:
    def searchInsert(self, nums, target) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)>>1
            print(mid)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                if mid == 0:
                    return 0
                if target > nums[mid-1]:
                    return mid
                else:
                    end = mid - 1
            else:
                if mid == len(nums)-1:
                    return len(nums)
                if target < nums[mid+1]:
                    return mid+1
                else:
                    start = mid + 1

s = Solution()
print(s.searchInsert([1,3], 2))