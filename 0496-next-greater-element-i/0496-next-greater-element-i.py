class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        maps = {}
        ans = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            maps[nums1[i]] = i
            
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                if nums2[top] in maps:
                    idx = maps[nums2[top]]
                    ans[idx] = nums2[i]
            
            stack.append(i)
            
        return ans