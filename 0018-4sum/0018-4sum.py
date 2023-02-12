class Solution:
    def fourSum(self, nums, target):
        
        nums.sort()
        
        n = len(nums)
        ans = []     
        
        for i in range(n):    
            for j in range(i + 1, n):
                num = target - nums[i] - nums[j]
                
                left, right = j + 1, n - 1

                while left < right:
                    if nums[left] + nums[right] < num:
                        left += 1
                    elif nums[left] + nums[right] > num:
                        right -= 1
                    else:
                        ans.append((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

        return list(set(ans))