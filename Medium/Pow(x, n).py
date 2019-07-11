class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        exp = abs(n)

        temp = x
        res = 1
        while exp>0:
            if exp & 1 == 1:
                res = res * temp
            exp = exp >> 1
            temp *= temp

        return res if n > 0 else 1 / res

s = Solution()
print(s.myPow(2.1, 3))