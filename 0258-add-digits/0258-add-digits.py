class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=0
        if num<=9:
            return num
        else:
            while(len(str(num))!=1):
                a=0
                l=list(str(num))
                for i in l:
                    a+=int(i)
                num=a
        return num