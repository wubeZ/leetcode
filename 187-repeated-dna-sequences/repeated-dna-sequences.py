class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int)
        
        def getMask(seq):
            mask = 0
            for i in range(10):
                if seq[i] == 'A':
                    mask |= (1<<i)
            
            for i in range(10,20):
                if seq[i%10] == 'C':
                    mask |= (1<<i)
            
            for i in range(20,30):
                if seq[i%10] == 'T':
                    mask  |= (1<<i)
            
            for i in range(30,40):
                if seq[i%10] == 'G':
                    mask |= (1<<i)
        
            return mask
        
        n = len(s) - 9
        ans = []
        for i in range(n):
            temp = s[i:i+10]
            mask = getMask(temp)
            if d[mask] == 1:
                ans.append(temp)
            
            d[mask] += 1
        
        return ans
            
