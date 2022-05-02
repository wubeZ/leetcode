class TireNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class WordDictionary:

    def __init__(self):
        self.root = TireNode()

    def addWord(self, word: str) -> None:
        current = self.root
        
        for w in word:
            if w not in current.children:
                current.children[w] = TireNode()
            current = current.children[w]
        
        current.isWord = True
        

    def search(self, word: str) -> bool:
        current = self.root
        
        def dfs(idx, current):
            
            for i in range(idx, len(word)):
                w = word[i]
                if w == ".":
                    for j in current.children.values():
                        if dfs(i+1 , j): 
                            return True
                    return False
                else:    
                    if w not in current.children:
                        return False
                    current = current.children[w]
            
            return current.isWord
        
        return dfs(0, current)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)