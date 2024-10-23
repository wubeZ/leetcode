class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = len(nums1) - len(nums2) - 1
        ptr2 = len(nums2) - 1
        ptr3 = len(nums1) - 1
        
        
        while (ptr1 > -1 and ptr2 > -1) or (ptr1 < 0 and ptr2 > -1):
            if ptr1 > -1 and nums1[ptr1] >= nums2[ptr2]:
                nums1[ptr3] = nums1[ptr1]
                ptr3 -= 1
                ptr1 -= 1
            else:
                nums1[ptr3] = nums2[ptr2]
                ptr3 -= 1
                ptr2 -= 1
        
        
        # while ptr2 > -1:
        #     nums1[ptr3] = nums2[ptr2]
        #     ptr2 -= 1
        #     ptr3 -= 1
        
        
        
                
        