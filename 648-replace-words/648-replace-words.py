class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        current = self.root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        
        current.isWord = True 
    
    def replaceWord(self, word): 
        current = self.root

        for idx in range(len(word)):
            w = word[idx]
            if w not in current.children:
                return word
            current = current.children[w]
            if current.isWord:
                return word[:idx + 1]
		
        return word
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for w in dictionary:
            self.add(w)    
        ans = []
        sentence = sentence.split()
                
        for word in sentence:
            res = self.replaceWord(word)
            ans.append(res)
            
        return " ".join(ans)
                