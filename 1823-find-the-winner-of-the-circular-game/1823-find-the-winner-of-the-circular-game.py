class Solution:
    
    def solve(self, arr, k, idx):
        if len(arr) == 1:
            return arr[0]
        
        last_idx = (idx + k - 1) % len(arr)
        arr.pop(last_idx)
        
        return self.solve(arr, k , last_idx)
    
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        
        return self.solve(arr, k , 0)