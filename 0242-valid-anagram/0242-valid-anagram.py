class Solution(object):
    def isAnagram(self, s, t):
        string1 = "".join(sorted(s))
        string2 = "".join(sorted(t))
        if string1.lower() == string2.lower():
            return True
        else:
            return False
            

        