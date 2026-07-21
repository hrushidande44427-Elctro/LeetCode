class Solution(object):
    def reverseWords(self, s):
        words =s.split()
        rev_words = []
        for i in range(len(words)-1,-1,-1):
            rev_words.append(words[i])
        string = " ".join(rev_words)
        return string

        