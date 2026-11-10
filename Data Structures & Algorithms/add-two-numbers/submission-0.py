# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #iteratre l1 and l2 simultaneously
        #take l1.val = l1.val + l2.val, cur_node1, cur_node2

        cur_node1 = l1 #head of l1
        cur_node2 = l2 #head of l2
        result = ListNode(0)  # dummy head, never returned
        ptr = result          # tail pointer that moves forward
        carry = 0

        # keep going while either list still has digits
        while cur_node1 or cur_node2:
            cur_sum = carry

            if cur_node1:
                cur_sum += cur_node1.val
                cur_node1 = cur_node1.next

            if cur_node2:
                cur_sum += cur_node2.val
                cur_node2 = cur_node2.next

            carry = cur_sum // 10   # tens digit goes to the next column
            digit = cur_sum % 10    # ones digit stays in this column

            ptr.next = ListNode(digit)
            ptr = ptr.next

        # leftover carry, e.g. 5 + 5 -> [0, 1]
        if carry:
            ptr.next = ListNode(carry)

        return result.next
'''
Let n be the length of l1 and m be the length of l2.
- Time: O(max(n, m)) — we traverse both lists once.
- Space: O(max(n, m)) — we create a new linked list to hold the answer.
'''


        