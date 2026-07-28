class Solution(object):
    def smallestPalindrome(self, s):
        half_len = len(s)//2

        base = sorted(s[:half_len])
        middle = [s[half_len]] if len(s)%2==1 else []
        rev_base = base[::-1]
        return "".join(base + middle + rev_base)
        