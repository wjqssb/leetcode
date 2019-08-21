class Solution:
    def __init__(self):
        self.res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.helper(1, [], n, k)
        return self.res
    def helper(self, first, l, n, k):
        if len(l) == k:
            self.res.append(l.copy())
        for i in range(first, n+1):
            l.append(i)
            self.helper(i+1, l, n, k)
            l.pop(-1)