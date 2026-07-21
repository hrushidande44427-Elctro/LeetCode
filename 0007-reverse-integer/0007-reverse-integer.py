class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        MAX = 2**31 - 1
        res = 0

        while x:
            digit = x % 10
            x //= 10

            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return 0

            res = res * 10 + digit

        res *= sign

        if res < -(2**31) or res > 2**31 - 1:
            return 0

        return res





        
        