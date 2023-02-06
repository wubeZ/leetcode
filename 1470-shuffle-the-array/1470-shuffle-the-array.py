class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = [nums[i] for i in range(n-1,-1,-1)]
        y = [nums[i] for i in range(len(nums)-1, n-1,-1)]
        ans = []
        
        for i in range(len(nums)):
            if i%2 == 0:
                ans.append(x.pop())
            else:
                ans.append(y.pop())
                
        return ans