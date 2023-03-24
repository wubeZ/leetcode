class Solution:
    def merge(self, a, b):
        c = []
        len1 = len(a)
        len2 = len(b)
        i , j = 0, 0
        while i < len1 and j < len2:
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        
        while i < len1:
            c.append(a[i])
            i += 1
        
        while j < len2:
            c.append(b[j])
            j += 1
        
        return c
        
    def mergesort(self, l, r, nums):
        if l >= r:
            return [nums[l]]
        
        mid = l + (r - l)//2
        
        leftHalf = self.mergesort(l, mid, nums)
        rightHalf = self.mergesort(mid + 1, r, nums)
        
        return self.merge(leftHalf, rightHalf)
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = self.mergesort(0, len(nums)-1, nums)
    
        return arr[-k]