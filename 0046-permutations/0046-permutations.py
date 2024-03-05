class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        
        def build():
            if len(cur) == len(nums):
                ans.append(cur[:])
                return 
        
            for idx, val in enumerate(nums):
                if val not in cur:
                    cur.append(val)
                    build()      
                    cur.pop()
                
                
        build()
        
        return ans