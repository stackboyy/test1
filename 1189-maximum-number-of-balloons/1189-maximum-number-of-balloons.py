class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b=0
        a=0
        l=0
        o=0
        n=0
        l=[]
        count=0
        for i in text:
            if i =="b":
                l.append(i)
            elif i =="a":
                l.append(i)
            elif i=="l":
                l.append(i)
            elif i=="o":
                l.append(i)
            elif i=="n":
                l.append(i)
        t=True
        while(t):
            for i in "balloon":
                if i in l:
                    l.remove(i)
                    count+=1
                else:
                    t=False
        return count//7


        