# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #after fast and slow
        #2,4,6,8,10 -- slow -> 6 and fast -> None

        #now reverse the second half
        second = slow.next
        prev, slow.next = None, None #break and make 6-> None
        while second: #second not none
            temp = second.next
            second.next = prev
            prev = second 
            second = temp
        #after reversing and breaking we get:
        # 2->4->6-> None
        # 10->8->None
        #prev -> 10
        
        #now merge
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
 