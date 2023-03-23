class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        path = ["0"] * n
        numset = set(nums)
        
        def backtrack(idx):
            if idx >= n:
                candidate = "".join(path[:])
                if candidate not in numset:
                    return (True, candidate)
                return (False, candidate)
            
            for i in range(idx, n):
                path[i] = "1"
                flag, value = backtrack(i + 1)
                if flag:
                    return (flag, value)
                path[i] = "0"
                
            flag, value = backtrack(idx + 1)
            
            return (flag, value)
        
        ans = backtrack(0)
        
        return ans[1]