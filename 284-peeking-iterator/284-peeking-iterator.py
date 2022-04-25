class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        
        if self.iterator.hasNext():
            self.pointer = self.iterator.next()
        else:
            self.pointer = None

    def peek(self):
        return self.pointer
        
    def next(self):
        nxtval = self.pointer
        
        if self.iterator.hasNext():
            self.pointer = self.iterator.next()
        else:
            self.pointer = None
            
        return nxtval
        
    def hasNext(self):
        return self.pointer is not None
               
    
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

