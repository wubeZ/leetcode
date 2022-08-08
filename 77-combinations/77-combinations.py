class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        
        def backtrack(nums,path):   
            if len(path) == k:
                result.append(path)
                return
        
            
            for i in range(len(nums)):
                backtrack(nums[i+1:], path + [nums[i]])
                
        
        
        
        result = []
        
        backtrack(nums,[])
        
        return result