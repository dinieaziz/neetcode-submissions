# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to signify first node
        dummy = ListNode() 
        
        newList = dummy
        while list1 and list2:
            # If list1 value is lower, it becomes the head
            if list1.val < list2.val:
                # Assign the lowest value to newList
                newList.next = list1

                # Move to next node
                list1 = list1.next
            # Else list2 value is lower, it becomes the head
            else:
                # Assign the lowest value to newList, then make the value become the head 
                newList.next = list2

                # Move to next node
                list2 = list2.next
            newList = newList.next

        # Attached remaining nodes
        newList.next = list1 or list2

        return dummy.next