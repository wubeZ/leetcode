class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        map = defaultdict(int)
        for i in arr:
            map[-i%k] += 1
        total = 0
        
        for i in arr:
            if i%k in map and map[-i%k] > 0:
                if i%k == -i%k and map[i%k] < 2:
                    continue
                total += 2
                map[i%k] -= 1
                map[-i%k] -= 1
                
        return total == len(arr)
                
            