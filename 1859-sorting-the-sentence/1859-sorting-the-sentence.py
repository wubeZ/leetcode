class Solution:
    def sortSentence(self, s: str) -> str:
        
        temp = []
        for w in s.split(" "):
            temp.append((w[-1], w[:-1]))
        
        temp.sort()
        
        ans = []
        for i, word in temp:
            ans.append(word)
        
        return " ".join(ans)