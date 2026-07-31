class Solution(object):
    def plusOne(self, digits):
        a=""
        l=[]
        for i in digits:
            a+=str(i)
        a=int(a)+1
        a=list(str(a))
        for j in a:
            l.append(int(j))
        return l

        