class Solution(object):
    def removeElement(self, nums, val):
        for i in range (nums.count(val)):
            nums.remove(val)
        print(len(nums),nums)
        