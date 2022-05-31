class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num = 1 << k
        seen = set()

        for i in range(k, len(s)+1):
            val = s[i-k:i]
            if val not in seen:
                seen.add(val)
                num -= 1
                if num == 0:
                    return True
                
        return False
            
        