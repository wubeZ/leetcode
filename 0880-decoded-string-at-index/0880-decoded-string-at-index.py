class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        slen = 0
        
        while slen != k:
            slen = 0
            last = ''
            
            for i in range(len(s)):
                if s[i].isdigit():
                    slen *= int(s[i])
                else:
                    slen += 1
                    last = s[i]
                    
#               if it is between the current digit multiple 
                if slen > k:
                    slen = slen//int(s[i]) 
                    k = k%slen
                    break
                elif slen == k:
                    return last
                
            if k == 0:
                return last