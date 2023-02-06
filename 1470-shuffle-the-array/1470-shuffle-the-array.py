class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ans = []
        xPtr = 0
        yPtr = n
        for i in range(len(nums)):
            if i%2 == 0:
                ans.append(nums[xPtr])
                xPtr += 1
            else:
                ans.append(nums[yPtr])
                yPtr += 1
                
        return ans