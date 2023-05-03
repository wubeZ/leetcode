class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [set(),set()]
        nums1set = set(nums1)
        nums2set = set(nums2)
        
        for num in nums1:
            if num not in nums2set:
                ans[0].add(num)
        
        for num in nums2:
            if num not in nums1set:
                ans[1].add(num)
                
        return ans