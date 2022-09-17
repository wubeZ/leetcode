class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = [int(x) for x in nums]
        arr.sort()
        return str(arr[-k])