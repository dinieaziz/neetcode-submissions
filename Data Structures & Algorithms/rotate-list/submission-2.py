# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If head is none, return as is
        # Get length of list
        # Denote number of rotations using %
            # If same as list size, return as is
        # Go to pivot position
        # Take current next as new head (start of list)
        # Set current next to null (end of list)
        # Attach initial start of list to the tail (reuse the length of list pointer)

        if head == None:
            return head

        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        rotations = k % length
        if rotations == 0:
            return head

        current = head
        for i in range(length - rotations - 1):
            current = current.next
        
        # Denote new head to return
        newHead = current.next
        # Clear current as it is now end of list
        current.next = None
        # The old end of list now points to the initial head of list
        tail.next = head

        return newHead
