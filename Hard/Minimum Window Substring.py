class Solution:
    def minWindow(self, s, t):
        need = {}
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1

        window = {}
        left = 0
        right = 0
        res = ""
        res_len = len(s)
        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1
            right += 1

            while self.helper(need, window):
                c = s[left]
                window[c] -= 1
                left += 1

                temp = s[left-1:right]
                if len(temp)<=res_len:
                    res = temp
                    res_len = len(temp)
        return res

    def helper(self, need, window):
        for d in need:
            if d not in window:
                return False
            else:
                if window[d] < need[d]:
                    return False
        return True

s = Solution()
print(s.minWindow("ab", "a"))