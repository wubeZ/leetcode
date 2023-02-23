class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        counter = defaultdict(int)
        counter2 = Counter(t)
        length = float("inf")
        
        complete = 0
        
        l = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            
            if counter[s[r]] == counter2[s[r]]:
                complete += 1
            
            while l <= r and complete == len(counter2):
                if length > r - l + 1:
                    length = r - l + 1
                    ans = s[l : r + 1]
                    
                counter[s[l]]-= 1
                if counter[s[l]] < counter2[s[l]]:
                    complete -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                
                l += 1
        
        return ans
            
                
                
            