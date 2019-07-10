import collections
class Solution:
    def convertStr2Dict(self, s):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    def groupAnagrams(self, strs):
        l = []
        d = {}
        for w in strs:
            wd = self.convertStr2Dict(w)
            f = False
            for k in d:
                kd = self.convertStr2Dict(k)
                if wd == kd:
                    d[k].append(w)
                    f = True
            if not f:
                d[w] = [w]
        for k in d:
            l.append(d[k])

        return l

    def groupAnagrams_2(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # tuple可以作为dict的key,可哈希
            ans[tuple(count)].append(s)
        return [dict(ans)[d] for d in dict(ans)]
s = Solution()
print(s.groupAnagrams_2(["eat","tea","tan","ate","nat","bat"]))



