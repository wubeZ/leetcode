class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            
            cur = cur.children[w]
        
        cur.isword = True
        cur.word = word
        
    
    def find(self, word):
        cur = self.root
            
        for w in word:
            if cur.isword:
                return cur.word

            if w not in cur.children:
                return word

            cur = cur.children[w]
            
        return word
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        for w in dictionary:
            self.add(w)
        
        ans = []
        for word in sentence.split(" "):
            ans.append(self.find(word))
                
        
        return " ".join(ans)