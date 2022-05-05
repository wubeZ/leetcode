class TireNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Solution:
    def __init__(self):
        self.root = TireNode()
    
    
    def add(self, word):
        current = self.root
        
        for w in word:
            if w not in current.children:
                current.children[w] = TireNode()
            current = current.children[w]

        current.isWord = True
    
    def construct(self, word):
        current = self.root
        
        for w in word:
            if w not in current.children or (current != self.root and  not current.isWord):
                return False
            current = current.children[w]
        
        return True
        
    def longestWord(self, words: List[str]) -> str:    
        ans = ""
        for word in words:
            self.add(word)
    
        for word in words:
            if len(ans) <= len(word) and self.construct(word):
                if len(ans) == len(word):
                    ans = min(ans, word)
                else:
                    ans = word
        
        return ans
                
            
    
            
            

        