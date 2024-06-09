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
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        for w in dictionary:
            self.add(w)
        
        ans = []
        for word in sentence.split(" "):
            cur = self.root
            flag = False
            c = 0
            for w in word:
                if cur.isword:
                    ans.append(cur.word)
                    break
                    
                if w not in cur.children:
                    flag = True
                    break
                    
                cur = cur.children[w]
                c += 1
            
            if flag or c == len(word):
                ans.append(word)
                
        
        return " ".join(ans)