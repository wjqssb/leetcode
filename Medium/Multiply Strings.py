class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        resL = []
        for i in range(len(num1)):
            temp = str(int(num1[len(num1) - 1 - i]) * int(num2))
            temp += '0' * i
            resL.append(temp)
        res = '0'
        print(resL)
        for i in range(len(resL)):
            if len(resL[i]) >= len(res):

                res = self.strAdd(resL[i], res)
            else:

                res = self.strAdd(res, resL[i])

            print(i, res)

        return res

    def strAdd(self, s1, s2):
        rs1 = s1[::-1]
        rs2 = s2[::-1]
        res = ''
        if len(rs1) >= len(rs2):
            n = 0
            for i in range(len(rs1)):
                if i <= len(rs2) - 1:
                    cur_sum = int(rs1[i]) + int(rs2[i]) + int(n)
                    if cur_sum > 9:
                        n = 1
                        res += str(cur_sum - 10)
                    else:
                        n = 0
                        res += str(cur_sum)
                else:
                    cur_sum = int(rs1[i]) + int(n)
                    if cur_sum > 9:
                        n = 1
                        res += str(cur_sum - 10)
                    else:
                        n = 0
                        res += str(cur_sum)
            if n:
                res += '1'
        return res[::-1]

s = Solution()
print(s.multiply('2132', '0'))