class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.number = None

class Solution:
    def __init__(self):
        self.node = TrieNode()
    
    def insert(self, word, num):
        cur = self.node
        
        for w in word:
            ind = int(w)
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        
        cur.number = num
        
    
    def search(self, word):
        cur = self.node
        
        
        for w in word:
            
            needed = 1 if w == "0" else 0
            indw = int(w)
            
            if cur.children[needed]:
                cur = cur.children[needed]
            else:
                cur = cur.children[indw]
            
        return cur.number
                
            
            
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxx = 0
        arr = []
        for num in nums:
            string = bin(num)[2:]
            left = 32 - len(string)
            string = "0" * left + string
            arr.append(string)
            self.insert(string, num)
        
        
        for i in range(len(nums)):
            num = nums[i]
            string = arr[i]
            
            comp = self.search(string)
            maxx = max(maxx, comp ^ num)
        
        
        return maxx
            