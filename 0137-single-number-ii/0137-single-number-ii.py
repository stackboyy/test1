class Solution(object):
    def singleNumber(self, nums):
        a=0
        for i in nums:
            if nums.count(i)!=3:
                a=i
        return a