# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count the length of the list in 1 pass
        curNode = head
        length = 0
        while curNode is not None:
            length += 1
            curNode = curNode.next
        
        if length == n:
            return head.next
            
        curNode = head
        for _ in range(length -n - 1):
            curNode = curNode.next
        
        curNode.next = curNode.next.next

        return head

        