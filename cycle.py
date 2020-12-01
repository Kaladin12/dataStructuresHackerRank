class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def add_next(self,nextV):
        self.next = SinglyLinkedListNode(nextV)
    def getNext(self):
        return self.next;

def has_cycle(head):
    if (not head):
        print(0)
        return
    else:
        nextN = head.getNext()
        while (nextN):
            if (nextN.data == head.data):
                print(1)
                return
            nextN = nextN.getNext()
        print(0)
    
e = SinglyLinkedListNode(0)
head = e
for i in range(1,20):
    e.add_next(i)
    e = e.getNext()
e.add_next(0)
has_cycle(head)