class Solution(object):
    def reverse(self, x):
        if x>=0:
            z=str(x)
            a=int(z[::-1])
            if a<=(2**31)-1:
                return a
            else :
                return 0
        elif x<0:
            z=str(x)
            b=-1*int(z[:0:-1])
            if b>=(-2**31):
                return b
            else:
                return 0
        else:
            return 0
        