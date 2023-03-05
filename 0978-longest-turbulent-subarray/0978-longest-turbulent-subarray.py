class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        
        greater_than = 1
        less_than = 1
        
        if len(arr) == 1:
            return 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                greater_than = less_than + 1
                less_than = 1
            elif arr[i] < arr[i-1]:
                less_than = greater_than + 1
                greater_than = 1
            else:
                greater_than = 1
                less_than = 1
        
            ans = max(ans, greater_than, less_than)
        
        return ans
                