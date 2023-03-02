class Solution:
    def compress(self, chars: List[str]) -> int:
        
        count = 0
        
        r = 0
        ind = 0
        
        while r < len(chars):
            w = 1
            while r + w < len(chars) and chars[r] == chars[r + w]:
                w += 1
                
            chars[ind] = chars[r]
            ind += 1
            count += 1
            
            if w > 1:
                number = str(w)
                for ch in range(len(number)):
                    chars[ind] = number[ch]
                    ind += 1
                count += len(str(w))
                
            r += w
        
        return count