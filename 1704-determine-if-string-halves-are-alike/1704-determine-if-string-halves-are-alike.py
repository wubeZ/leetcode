class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def check(start, end):
            count = 0
            for i in range(start , end):
                if s[i] in 'aeiouAEIOU':
                    count += 1
            return count
        
        return check(0,len(s)//2) == check(len(s)//2,len(s))