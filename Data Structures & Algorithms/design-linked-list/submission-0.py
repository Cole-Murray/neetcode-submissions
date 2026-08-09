class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        i = index
        curr = self.head.next
        while i > 0:
            curr = curr.next
            i-=1

        return curr.val            

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next.prev = new 
        self.head.next = new
        new.prev = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.tail
        new.prev = self.tail.prev
        self.tail.prev.next = new
        self.tail.prev = new
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        new = ListNode(val)
        curr = self.head
        if index > self.size:
            return

        while index >= 0:
            curr = curr.next
            index -= 1
        
        left = curr.prev
        right = curr

        new.prev = left
        new.next = right
        left.next = new
        right.prev = new

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index >= self.size:
            return
            
        while index >= 0:
            curr = curr.next
            index -= 1

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)