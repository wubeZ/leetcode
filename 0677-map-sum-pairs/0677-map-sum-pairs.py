class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        
        for w in key:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.isWord = val
        
        
    def getSum(self, cur):
        if len(cur.children.keys()) == 0:
            return cur.isWord
        
        count = 0
        for next_child in cur.children.keys():
            count += self.getSum(cur.children[next_child])
        
        return count + cur.isWord
            
        
    def sum(self, prefix: str) -> int:
        
        ans = 0
        cur = self.root
        
        for w in prefix:
            if w not in cur.children:
                return 0
            else:
                cur = cur.children[w]
        
        ans += cur.isWord
        
        if len(cur.children.keys()) != 0:
            ans -= cur.isWord
            ans += self.getSum(cur)
        
        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)