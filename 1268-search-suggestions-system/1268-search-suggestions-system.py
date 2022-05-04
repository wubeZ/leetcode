class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.key = []  # get the sorted keys at this level
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        current = self.root
        for w in word:
            if w not in current.children:
                current.key.append(w)
                current.key.sort()
                current.children[w] = TrieNode()
            current = current.children[w]
        current.isWord = True
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        current = self.root
        #insert to trie
        for w in products:
            self.add(w)
        #get the word from trie
        def getword(word, child):
            if len(wlist) == 3:
                return
            if child.isWord:
                wlist.append(prefix + word)
                
            for i in child.key[:3]:
                cur_word = word
                cur_word += i
                getword(cur_word, child.children[i])
        
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            if searchWord[i] not in current.children:
                for j in range(i,len(searchWord)):
                    res.append([])
                break
            else:    
                wlist = []
                getword("", current.children[searchWord[i]])
                res.append(wlist)
                current = current.children[searchWord[i]]
            

        return res
            
            
            
            
            
                    