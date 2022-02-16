class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        answer = []
        length = len(nums)
        k = k % length
        pointer = length - k
        
        for i in range(pointer,length):
            answer.append(nums[i])
        
        for i in range(pointer-1,-1,-1):
            nums[i+k] = nums[i]
        
        for i in range(len(answer)):
            nums[i] = answer[i]