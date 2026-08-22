class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        p=1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        a=s+p
        if n%a==0:
            return True
        else :
            return False

        