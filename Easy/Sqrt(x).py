class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        left = 1
        right = x//2
        while left<right:
            mid = (left+right+1)>>1

            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid-1
        return left

s = Solution()
print(s.mySqrt(4))
