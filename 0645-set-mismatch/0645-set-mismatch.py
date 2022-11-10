class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums)+1)
        for n in nums:
            res[n] += 1
        ans = []
        for i in range(1,len(res)):
            if len(ans) == 1:
                break
            if res[i] == 2:
                ans.append(i)
        for i in range(1,len(res)):
            if len(ans) == 2:
                break
            if res[i] == 0:
                ans.append(i)
        return ans