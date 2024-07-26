class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def printLinkedListReverse(node):
    if node is None:
        return
    printLinkedListReverse(node.next)
    print(node.val, end=" ")

A = ListNode(4)
A.next = ListNode(3)
A.next.next = ListNode(2)
A.next.next.next = ListNode(1)
A.next.next.next.next = ListNode(0)

printLinkedListReverse(A)
print()

