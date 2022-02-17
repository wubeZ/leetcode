class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        i = index - 1
        while i >= 0:
            temp = temp.next
            i -= 1   
        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size +=1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif 0 < index < self.size:
            temp = self.head
            i = index - 1
            while i > 0:
                temp = temp.next
                i -= 1
            newNode = ListNode(val)
            newNode.next = temp.next
            temp.next = newNode
            self.size +=1
        elif index == self.size:
            self.addAtTail(val)
        else:
            return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            newNode = self.head
            self.head = newNode.next
            del newNode
        else:
            temp = self.head 
            i = index - 1
            while i:
                temp = temp.next
                i -= 1
            newNode = temp.next
            temp.next = newNode.next
            del newNode
        self.size -=1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)