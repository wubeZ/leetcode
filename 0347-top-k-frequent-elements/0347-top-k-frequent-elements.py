class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        for key , val in counter.items():
            ans.append((key, val))
            
        ans.sort(key = lambda x: x[1], reverse = True)
        
        return [elem[0] for i, elem in enumerate(ans) if i < k ]
        