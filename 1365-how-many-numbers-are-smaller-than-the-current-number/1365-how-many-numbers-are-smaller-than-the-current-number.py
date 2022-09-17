class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()
        
        ans = [0] * len(nums)
        i = 0
        while i < (len(arr)):
            count = i
            if i != 0 and arr[i-1][0] == arr[i][0]:
                while i < len(arr) and i != 0 and arr[i-1][0] == arr[i][0]:
                    ans[arr[i][1]] = count-1
                    i += 1
            else:
                ans[arr[i][1]] = count
                i += 1
            
        return ans
            