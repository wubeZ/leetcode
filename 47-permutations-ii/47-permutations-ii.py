class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        def backtrack(counter, path):
            if len(path) == n:
                result.append(path)
                return
            
            for i in counter:
                if counter[i] > 0:
                    counter[i] -= 1
                    backtrack(counter,path + [i])
                    counter[i] += 1
        
        
        result = []
        
        backtrack(Counter(nums), [])
        
        return result