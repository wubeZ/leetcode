class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_Sum = [0]
        sumResult = 0
        for val in nums:
            sumResult += val
            prefix_Sum.append(sumResult)
          
        index = 0
        while index < len(nums):
            if prefix_Sum[index] == prefix_Sum[len(nums)] - prefix_Sum[index + 1]:
                return index
            else:
                index += 1
        
        return -1