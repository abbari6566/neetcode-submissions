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

        '''
        Fast and slow pointer solution:
        ---------------------------------------------------------------------------
        dummy = ListNode(0,head) #takes value 0 and points to head
        slow = dummy
        fast = dummy

        #move fast exactly n steps ahead of slow
        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        #at this point n is point the (n-1)th node
        slow.next = slow.next.next

        return dummy.next

        *********************************************
        Both Solution time complexity almost same O(N)
        **********************************************
        '''

        