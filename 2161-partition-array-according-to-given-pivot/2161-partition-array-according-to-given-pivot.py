class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, greater, equals = [], [], []
        for i in range(len(nums)):
            if nums[i] == pivot:
                equals.append(nums[i])
            elif nums[i] > pivot:
                greater.append(nums[i])
            else:
                less.append(nums[i])
                
        return less + equals + greater
            
        