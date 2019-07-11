class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[0])

        i = 0
        while i < len(intervals)-1:
            pre = intervals[i]
            post = intervals[i+1]

            if pre[1] >= post[0]:
                intervals.remove(pre)
                intervals.remove(post)
                intervals.insert(i, [pre[0], max(pre[1], post[1])])
            else:
                i += 1
        return intervals

    def merge_2(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res



s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))