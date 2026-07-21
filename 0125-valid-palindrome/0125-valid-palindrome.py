class Solution(object):
    def isPalindrome(self, s):
        string = "".join(c for c in s if c.isalnum())
        rev = string[::-1]
        if rev.lower()==string.lower():
            return True
        else:
            return False
       
        