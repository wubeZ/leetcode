class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        if len(nums1) %2 == 0:
            mid = len(nums1)//2
            return float((nums1[mid-1] + nums1[mid])/2)
        else:
            mid = len(nums1)//2
            return float(nums1[mid])