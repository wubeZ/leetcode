class Solution:
    def reverseWords(self, s: str) -> str:
        r = []
        for word in s.split(" "):
            reverse = word[::-1]
            r.append(reverse)
        
        return " ".join(r)
            
            