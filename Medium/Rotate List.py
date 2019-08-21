
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next

        y = k%l
        tail.next = head
        for i in range(l-y):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
