class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur =  cur.children[w]
        
        cur.isWord = True
    
    def dfs(self, idx, cur, word):
        
        for i in range(idx, len(word)):
            w = word[i]
            if w not in cur.children:
                if w == ".":
                    for key in cur.children.keys():
                        isValid = self.dfs(i + 1, cur.children[key], word)
                        if isValid:
                            return True
                return False
            cur = cur.children[w]
        
        return cur.isWord
    
    def search(self, word: str) -> bool:
        cur = self.root
        return self.dfs(0, cur, word)    
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)