class Solution:
    def partition(self, l, r, nums):
        
        pivot_element = nums[r]
        
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot_element:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        
        return i + 1
        
    def quicksort(self, l, r, nums):
        if l >= r:
            return
        
        mid = self.partition(l, r , nums)
        
        leftHalf = self.quicksort(l, mid - 1, nums)
        rightHalf = self.quicksort(mid + 1, r, nums)
        
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.quicksort(0, len(nums)-1, nums)
        
        return nums[-k]