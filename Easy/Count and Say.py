class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(1, n):
            curr = ''
            count = 0
            s = None
            for j in range(len(res)):
                if j == 0:
                    count = 1
                    s = res[j]
                else:
                    if res[j] == res[j - 1]:
                        count += 1
                    elif res[j] != res[j - 1]:
                        curr = curr + str(count) + s
                        count = 1
                        s = res[j]
                if j == len(res) - 1:
                    curr = curr + str(count) + s
            res = curr

        return res

s = Solution()
print(s.countAndSay(4))