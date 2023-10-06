class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pref_max = []
        suf_max = []
        
        max_num = 0
        for i in range(len(nums)):
            max_num = max(max_num, nums[i])
            pref_max.append(max_num)
        max_num = 0
        for i in range(len(nums)-1,-1,-1):
            max_num = max(max_num, nums[i])
            suf_max.append(max_num)
        
        suf_max = suf_max[::-1]
        
        ans = 0
        for i in range(1, len(nums)-1):
            temp = (pref_max[i-1] - nums[i]) * suf_max[i+1] 
            ans = max(ans, temp)
            
        return ans