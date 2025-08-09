# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy # Tail pointer to track the end of the merged list
        # Merged until one list is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 # Link tail to list1's current node
                list1 = list1.next # Move list1 forward 
            else:
                tail.next = list2 # Link tail to list2's current node
                list2 = list2.next # Move list2 forward
            tail = tail.next # Move tail forward to the last
        # Attach the remaining part of list1 or list2
        tail.next = list1 or list2 
        # Return the merged list starting from dummy.next
        return dummy.next
        


