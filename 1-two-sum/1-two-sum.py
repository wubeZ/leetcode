class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        heap = []
        ans = []
        sortlist = []
        left = 0
        right = len(nums) -1
        for i in range(len(nums)):
            sortlist.append((nums[i],i))

        sortlist.sort()
        
        while left < right:
            if sortlist[left][0] + sortlist[right][0] < target:
                left += 1
            elif sortlist[left][0] + sortlist[right][0] > target:
                right -= 1
            elif sortlist[left][0] + sortlist[right][0] == target:
                ans.append(sortlist[left][1])
                ans.append(sortlist[right][1])
                break
            
        return ans