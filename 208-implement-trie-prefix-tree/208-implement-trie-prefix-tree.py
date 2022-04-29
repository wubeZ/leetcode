class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
            
        current.isWord = True
                
    def search(self, word, isPrefix = False) -> bool:
        current = self.root
        
        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]

        return current.isWord or isPrefix
        

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)