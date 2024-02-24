class Solution:
    def splitNum(self, num: int) -> int:
        nums = list(map(int, str(num)))
        nums.sort()
        
        nums1 = ""
        nums2 = ""
        
        for i, ele in enumerate(nums):
            if i % 2 == 0:
                nums1 += str(ele)
            else:
                nums2 += str(ele)
                
        
        return int(nums1) + int(nums2)