class Solution(object):
    def merge(self, nums1, m, nums2, n):
        count=0
        ch=m
        while(count<len(nums2)):
            if(nums1[ch]==0):
                nums1[ch]=nums2[count]
                count+=1
                ch+=1
        nums1.sort()
        