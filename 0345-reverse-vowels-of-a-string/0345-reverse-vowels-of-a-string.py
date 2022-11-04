class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowels.append(s[i])
        
        if len(vowels) == len(s):
            return s[::-1]
            
        lists = list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                lists[i] = vowels.pop()
        
        return "".join(lists)
            