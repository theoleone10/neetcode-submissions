# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        k = 0

        while node:
            node = node.next
            k += 1

        prev, curr = None, head

        print(k)
        for i in range(k-n): 
            prev = curr
            curr = curr.next
        if prev == None:
            head = curr.next
        else:
            prev.next = curr.next

        return head
        
        