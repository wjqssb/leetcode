class Solution:
    def __init__(self):
        self.l = []

    def combinationSum(self, candidates, target):
        candidates.sort()
        self.helper(0, [], candidates, target)
        return self.l

    def helper(self, index, currList, candidates, target):
        if target == 0:
            self.l.append(currList)
            return
        for i in range(index, len(candidates)):
            currVal = candidates[i]
            if target - currVal >= 0:
                self.helper(i, currList + [currVal], candidates, target - currVal)

            else:
                break


s = Solution()
print(s.combinationSum([8,7,4,3,3],11))