class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in list(s.split(" ")):
            if word.isalnum():
                ans.append(word)
            
        return " ".join(ans[::-1])
        