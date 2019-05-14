class Solution:
    def trap(self, height) -> int:
        left = []
        for i in range(len(height)):
            if i == 0:
                left.append(0)
            else:
                left.append(max(left[i - 1], height[i - 1]))
        print(left)
        right = []
        for i in reversed(list(range(len(height)))):
            if i == len(height) - 1:
                right.append(0)
            else:
                right.insert(0, max(right[0], height[i + 1]))
        print(right)

        res = 0
        for i in range(len(height)):
            res += max(0, min(left[i], right[i]) - height[i])

        return res

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))