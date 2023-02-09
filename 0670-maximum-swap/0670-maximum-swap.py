class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        first = True
        temp = None
        for i in range(len(nums)):
            max_idx = i
            j = i + 1
            while j < len(nums): 
                if nums[j] > nums[max_idx]:
                    max_idx = j
                j += 1
            if max_idx != i:
                
                if first:
                    first = False
                    to_swap = (nums[i], nums[max_idx])
                    temp = max_idx
                    nums[max_idx], nums[i] = nums[i], nums[max_idx]
                else:
                    if nums[i] in to_swap and nums[max_idx] in to_swap and i == temp:
                        nums[max_idx], nums[i] = nums[i], nums[max_idx]
                        temp = max_idx
                
        
        
        return int("".join(nums))