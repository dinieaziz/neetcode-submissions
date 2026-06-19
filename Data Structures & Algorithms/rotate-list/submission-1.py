# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get length of list
        # Denote number of rotation using % to get remainder
            # If same as list size, return
        # Get to pivot position
        # Take next as temp
        # Set next as null
        # Get to end
            # Put temp as next

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
        
        newHead = current.next
        current.next = None
        tail.next = head

        return newHead
