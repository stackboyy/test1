class Solution(object):
    def isPalindrome(self, s):
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i.lower())
        if a==a[::-1]:
            return True
        else:
            return False