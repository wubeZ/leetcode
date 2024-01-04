class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue  
            
            target = -1 *  nums[i]
            
            dictionary = {}
            for j in range(i+1, len(nums)):
                if nums[j] in dictionary:
                    val = (nums[i],dictionary[nums[j]] ,nums[j])
                    ans.add(val)
                    
                dictionary[target - nums[j]] = nums[j]
        
        return ans
            