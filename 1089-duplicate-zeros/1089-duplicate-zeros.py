class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        count, overflow = 0, False
        
        for i in range(len(arr)):
            count += 1
            if arr[i] == 0:
                count += 1
            if count > len(arr):
                overflow = True
                break
            if count == len(arr):
                break
            
        left = i 
        right = len(arr)-1
        
        if overflow:
            left -= 1
            right -= 1
        
        while left >= 0 and right >= 0:
            if arr[left] == 0:
                arr[right] = 0
                arr[right - 1] = 0
                right -= 1
            
            else:
                arr[right] = arr[left]
            left -= 1
            right -= 1
        
        if overflow:
            arr[-1] = 0
        
                    