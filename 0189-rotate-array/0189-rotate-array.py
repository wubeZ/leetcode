class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        l = len(nums) - k
        leftarr = nums[l:]
        rightarr = nums[:l]
        
        j = 0
        i = 0
        while i < len(leftarr):
            nums[j] = leftarr[i]
            j += 1
            i += 1
        i = 0
        while i < len(rightarr):
            nums[j] = rightarr[i]
            j += 1
            i += 1
        
        