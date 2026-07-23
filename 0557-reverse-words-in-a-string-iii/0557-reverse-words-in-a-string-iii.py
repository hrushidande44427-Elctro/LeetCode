class Solution(object):
    def reverseWords(self, s):
        words =s.split()
        rev_words = []
        for i in words:
            rev_words.append(i[::-1])
        rev = " ".join(rev_words)
        return rev



        
        