class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        
        def find(idx , k):
            if len(arr) == 1:
                return arr[0]
            
            last_idx = (idx + k - 1) % len(arr)
            
            arr.pop(last_idx)
            
            return find(last_idx, k)  
        
        
        return find(0,k)