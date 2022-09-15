class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0 : return []

        counter = Counter(changed)
        original = []
    
        for num in sorted(changed):
            if num in counter and (num * 2) in counter:
                original.append(num)
                if counter[num] > 1: counter[num] -= 1 
                else: del counter[num]
                if counter[num * 2] > 1: counter[num * 2] -= 1
                else: del counter[num*2]
            
        return original if not counter else []