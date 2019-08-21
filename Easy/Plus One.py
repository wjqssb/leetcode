class Solution:
    def plusOne(self, digits):
        i = len(digits)-1
        carry = 1
        while i >= 0:
            if carry:
                s = digits[i]+carry
                if s == 10:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            i -= 1
        if carry:
            return [1]+digits
        return digits

s = Solution()
print(s.plusOne([9,9,9]))