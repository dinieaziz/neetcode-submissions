# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse each node of each list
        # Add them together, carry over to next node if exceed 10
        # Shift to next nodes

        dummy = ListNode()
        result = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get the value of the nodes
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            # Calculate the remainder and carry
            total = l1Val + l2Val + carry
            remainder = total % 10              # Keep as current node
            carry = total // 10                  # Add to next node

            # Shift the nodes
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

            # Assign the remainder to result then shift the node
            result.next = ListNode(remainder)
            result = result.next
        
        return dummy.next