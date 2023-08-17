class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        arr = sorted(counter.keys(), reverse = True)
        if (counter[0] % 2 != 0):
            return False
        
        for num in arr:
            if counter[num] == 0:
                continue
            if num > 0:
                if (num / 2) not in counter or counter[num] > counter[(num / 2)]:
                    return False
                counter[(num / 2)] -= counter[num]
            else:
                if (num * 2) not in counter or counter[num] > counter[(num * 2)]:
                    return False
                counter[(num * 2)] -= counter[num]
                
        
        return True
            
        
        
        