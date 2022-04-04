class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num , max_num = min(nums), max(nums)
        res = []
        counter = Counter(nums)
        
        for i in range(min_num,max_num + 1):
            if counter[i] > 0:
                for j in range(counter[i]):
                    res.append(i)
        
        return res
            