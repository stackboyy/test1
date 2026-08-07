class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        x=nums1+nums2
        x.sort()
        m=len(nums1)
        n=len(nums2)
        a=m+n
        if (a%2==0):
            return float((x[a//2]+x[a//2-1])/2.0)
        else:
            return float(x[a//2])
