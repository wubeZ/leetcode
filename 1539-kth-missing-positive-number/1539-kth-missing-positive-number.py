class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = -1
        right = len(arr)
        
        while left + 1 < right:
            mid = left + (right - left) //2
            
            if arr[mid] - 1 - mid < k:
                left = mid
            else:
                right = mid
        
        return right + k