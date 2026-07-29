class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        start=False
        for i in range(len(s) - 1, -1, -1):
            if s[i]==" ":
                if start:
                    break
            else :
                start=True    
                count+=1

        return count