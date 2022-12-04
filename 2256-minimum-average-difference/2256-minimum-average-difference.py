class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        frontprefix = [0]
        for i in range(len(nums)):
            frontprefix.append(nums[i]+frontprefix[-1])
        backprefix = [0]
        for i in range(len(nums)-1,-1,-1):
            backprefix.append(nums[i]+backprefix[-1])
        
        backprefix = backprefix[::-1]
        frontprefix = frontprefix[1:]

        ans = 0
        maxval = float("inf")

        for i in range(len(nums)):
            x = frontprefix[i]//(i+1) if frontprefix[i] != 0 else 0 
            y = backprefix[i+1]//(len(nums)-i-1) if backprefix[i+1] != 0 else 0
            val = abs(x-y)
            if maxval > val:
                maxval = val
                ans = i
        
        return ans
        