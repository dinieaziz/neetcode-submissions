# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # Denote the next node
            nextNode = curr.next

            # Reverse the arrow direction
            curr.next = prev

            # Shift prev and current a step forward
            prev = curr
            curr = nextNode

        return prev