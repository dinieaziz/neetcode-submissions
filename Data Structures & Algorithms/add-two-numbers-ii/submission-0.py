# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        # Traverse each linked list
        # Add the nodes and denote the remainder if > 10
        # Shift to the next nodes

        # Create 2 stacks l1 and l2, append all into stack
        # Pop each, add and denote the remainder if > 10
        # Shift to next result node
        
        l1Stack, l2Stack = [], []

        while l1:
            l1Stack.append(l1.val)
            l1 = l1.next
            
        while l2:
            l2Stack.append(l2.val)
            l2 = l2.next

        result = None
        carry = 0

        while l1Stack or l2Stack or carry:
            l1Val = l1Stack.pop() if l1Stack else 0
            l2Val = l2Stack.pop() if l2Stack else 0

            total = l1Val + l2Val + carry
            remainder = total % 10              # To keep
            carry = total // 10                 # To bring over

            # Create a new node
            newNode = ListNode(remainder)
            # Add the node from the smallest order first
            newNode.next = result
            # Move to next higher order
            result = newNode
            
        return result
