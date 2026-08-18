class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        a=bin(n)[2:]
        for i in a:
            count+=int(i)
        return count
        