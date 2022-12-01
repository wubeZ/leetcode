class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c = 0
        for i in range(len(s)//2):
            if s[i] in 'aeiouAEIOU':
                c += 1
        cr = 0
        for i in range(len(s)//2, len(s)):
            if s[i] in 'aeiouAEIOU':
                cr += 1
        return c == cr