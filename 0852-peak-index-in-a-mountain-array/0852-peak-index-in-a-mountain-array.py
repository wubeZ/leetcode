class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr)-1
        
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if arr[mid-1] < arr[mid]:
                left = mid
            else:
                right = mid
        
        return left