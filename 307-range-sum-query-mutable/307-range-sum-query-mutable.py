class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = sum(nums)
        
    def update(self, index: int, val: int) -> None:
        self.sums -= self.nums[index]
        self.nums[index] = val
        self.sums += val

    def sumRange(self, left: int, right: int) -> int:
        if right - left > len(self.nums) //2:
            self.ans = sum(self.nums[:left] + self.nums[right + 1:])
            return self.sums - self.ans
        return sum(self.nums[left : right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)