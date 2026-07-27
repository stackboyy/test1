class Solution(object):
    def removeDuplicates(self, nums):
        count=0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                count+=1
            else:
                i += 1
        print(count,nums)
        