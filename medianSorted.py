import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i1 = len(nums1)-1
        i2 = len(nums2)-1
        m1 = 0
        m2 = 0
        
        if(i1 ==0):
            m1 = nums1[i1]
        if(i2 == 0):
            m2 = nums2[i2]
        
        if(i1 > 0):
            if(i1 % 2 == 0):
                m1 = nums1[i1//2]
            else:
                m1 = (nums1[math.floor(i1/2)]+nums1[math.ceil(i1/2)])/2

        if(i2 > 0):
            if(i2 % 2 == 0):
                m2 = nums2[i2//2]
            else:
                m2 = (nums2[math.floor(i2/2)]+nums2[math.ceil(i2/2)])/2
        
        if(m1 == m2):
            return m1
        if(m1 < m2):
            return Solution.findMedianSortedArrays(self,nums1[:math.floor(len(nums1)/2)],nums2[math.floor(len(nums2)/2):])
        if(m1 > m2):
            return Solution.findMedianSortedArrays(self,nums1[math.floor(len(nums1)/2):],nums2[:math.floor(len(nums2)/2)])
        if(i1 < 0):
            return m2
        else:
            return m1

print(Solution.findMedianSortedArrays(Solution,[1,3],[2,7]))