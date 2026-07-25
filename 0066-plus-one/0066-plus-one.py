class Solution(object):
    def plusOne(self, digits):
        integer = int("".join(map(str,digits)))
        integer +=1
        lis = list(map(int,str(integer)))
        return lis
        
       
        
        