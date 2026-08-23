class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        f=True
        c=1
        while(f):
            for i in str(n):
                c*=int(i)
            if c%t==0 :
                return int(n)
                break
            else:
                int(n)
                n+=1
                c=1
