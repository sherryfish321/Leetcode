# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle node: fast moves 2 steps and slow moves 1 step at a time.
        slow, fast = head, head.next
        while fast and fast.next: # Stop when fast reaches the end or cannot move 2 steps further
            slow = slow.next
            fast = fast.next.next
        # Reverse the list starting after "slow"
        second = slow.next # Starting the node of the second half list
        prev = slow.next = None # break the link between the halves

        while second:
            tmp = second.next # Temporarily store the next node to avoid losing the rest of the list 
            second.next = prev # Reverse the pointer
            prev = second # Move "prev" forward
            second = tmp # Move "second" forward 
        # Merge the two lists
        first, second = head, prev
        while second: # Iterate until second half is exhausted
            tmp1, tmp2 = first.next, second.next # Store next nodes before modifying links
            first.next = second # Link a node from the second-half
            second.next = tmp1 # Link the second-half node back to the next first-half node
            first, second = tmp1, tmp2 # Move both pointers forward
        # No return needed, the list is modified in place
        




        
