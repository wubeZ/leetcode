class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    
        wlen = len(words)
        wsize = len(words[0])
        
        i = 0
        res = []
        while i < (len(s)-(wlen*wsize)+1):
            j = i
            counter = d.copy()
            count = 0
            while j < (len(s)):
                cur = s[j:j+wsize]
                if cur not in counter or counter[cur] == 0: 
                    break
                if cur in counter:
                    counter[cur] -= 1
                    count += 1
                    
                if wlen == count:
                    res.append((j + wsize) - (wlen * wsize))
                    break
                j += wsize
            i += 1
                
        return res