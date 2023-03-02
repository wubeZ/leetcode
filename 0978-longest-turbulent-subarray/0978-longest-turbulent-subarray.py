class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        
        left = 0
        right = 1
        
        prev_sign = ""
        
        while right < len(arr):
            if arr[right - 1] == arr[right]:
                right += 1
                left = right - 1
                prev_sign = ""
                continue
            
            if arr[right - 1] < arr[right] and prev_sign != "<":
                ans = max(ans, right - left + 1)
                right += 1
                prev_sign = "<"
                
            elif arr[right - 1] > arr[right] and prev_sign != ">":
                ans = max(ans, right - left + 1)
                right += 1
                prev_sign = ">"
            else:
                left = right - 1
                prev_sign = ""
        
        
        return ans
                