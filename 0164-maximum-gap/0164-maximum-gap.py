class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff=0
        if len(nums)>1:
            a=nums.sort()
            for i in range(len(nums)-1):
                if nums[i+1]-nums[i]>diff:
                    diff=nums[i+1]-nums[i]
            return diff
        else:
            return 0

        