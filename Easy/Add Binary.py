class Solution:
    def addBinary(self, a, b):
        la = len(a)-1
        lb = len(b)-1
        carry = 0
        res = ''
        while la >= 0 and lb >= 0:
            s = int(a[la]) + int(b[lb]) + carry
            if s < 2:
                res = str(s)+res
                carry = 0
            else:
                res = str(s%2)+res
                carry = 1
            la -= 1
            lb -= 1

        while la >= 0:
            s = int(a[la])+carry
            if s == 2:
                res = '0'+res
                carry = 1
            else:
                res = str(s)+res
                carry = 0
            la -= 1
        while lb >= 0:
            s = int(b[lb])+carry
            if s == 2:
                res = '0'+res
                carry = 1
            else:
                res = str(s)+res
                carry = 0
            lb -= 1
        if carry:
            return '1'+res
        else:
            return res

s = Solution()
print(s.addBinary('1010', '1011'))