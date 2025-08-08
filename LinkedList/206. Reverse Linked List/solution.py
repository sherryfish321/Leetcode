# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # This will eventually become the new head of the reversed list
        while head:
            curr = head # Store the current head
            head = head.next # Move head one step forward
            curr.next = prev # Reverse the pointer direction
            prev = curr # Move prev forward: curr is now the last node in the reversed list
        return prev
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty, return None
        if not head:
            return None

        # Initially assume the new head is the current node
        newHead = head

        # Recursive case: if there is a next node, keep going deeper
        if head.next:
            # Recursively reverse the rest of the list
            newHead = self.reverseList(head.next)

            # Reverse the link: make head.next point back to head
            head.next.next = head  # ← 這一行將下一個節點的 next 指向目前的 head（關鍵步驟）
        
        # Sever the original forward link to avoid cycle
        head.next = None  # ← 將當前節點的 next 設為 None，是為了讓原先的第一個節點變成尾端

        # Return the new head of the reversed list
        return newHead
