class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self.node_remove(n)
            self.node_add(n)
            return n.val
        
        return -1

    def put(self, key, value):
        if key in self.dic:
            self.node_remove(self.dic[key])
        
        n = Node(key, value)
        
        self.node_add(n)
        self.dic[key] = n
        
        if len(self.dic) > self.capacity:
            n = self.head.next
            self.node_remove(n)
            del self.dic[n.key]

    def node_remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def node_add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)