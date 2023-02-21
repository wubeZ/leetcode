class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for ch in counter:
            if counter[ch] == 1:
                return ch
        