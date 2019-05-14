class Solution:

    def __init__(self):
        self.l = []

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.helper(0, [], candidates, target)
        return self.l

    def helper(self, index, currList, candidates, target):
        if target == 0:
            self.l.append(currList)
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]: continue
            currVal = candidates[i]
            if target - currVal >= 0:
                self.helper(i + 1, currList + [currVal], candidates, target - currVal)
            else:
                break

s = Solution()
print(s.combinationSum2([10,1,2,2,7,6,1,5], 8))