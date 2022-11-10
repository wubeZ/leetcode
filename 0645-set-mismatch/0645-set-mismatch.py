class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums)+1)
        for n in nums:
            res[n] += 1
        missing, doubled = None , None
        for i in range(1,len(res)):
            if missing and doubled:
                break
            if res[i] == 2:
                doubled = i
            if res[i] == 0:
                missing = i
        
        return [doubled, missing]
        