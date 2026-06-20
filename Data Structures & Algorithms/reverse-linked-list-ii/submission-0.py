# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Dummy node to handle edge case (start of list)
        # Go to left - 1 pointer
        # Track prev and curr
        # Reverse while right - left + 1
        # Update pointers
        # Return dummy.next

        # Start of list to handle edge cases
        dummy = ListNode(0, head)
        
        # Go to start of position to reverse
        leftPtr = dummy
        for _ in range(left - 1):
            leftPtr = leftPtr.next
        
        # Reverse the list for right - left +1
        prev, curr = None, leftPtr.next
        for _ in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        # Attach back remaining of the lists
        leftPtr.next.next = curr
        leftPtr.next = prev

        # Return the head of the list
        return dummy.next