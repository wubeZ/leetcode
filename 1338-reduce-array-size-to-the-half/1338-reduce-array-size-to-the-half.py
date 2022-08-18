class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mid = len(arr)//2
        ans = 0
        total = 0
        counter = Counter(arr)
        counter = list(counter.items())
        counter.sort(key = lambda x:x[1], reverse = True)
        
        for key, val in counter:
            if total >= mid:
                break
            ans += 1
            total += val
            
        return ans