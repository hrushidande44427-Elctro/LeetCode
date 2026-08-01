class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs :
            return ""
        first = strs[0]
        prefix = ""
        
        for i in range(len(first)):
            for word in strs:
                if i>=len(word):
                    return prefix
                if word[i] != first[i]:
                    return prefix
            prefix+=first[i]
        return prefix


        
                

            
                




        