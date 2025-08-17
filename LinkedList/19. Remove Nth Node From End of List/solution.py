class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)       # Step 1: Dummy before head
        fast = slow = dummy             # Step 2: Initialize two pointers

        for _ in range(n + 1):          # Step 3: Move fast n+1 steps ahead
            fast = fast.next

        while fast:                     # Step 4: Move both until fast hits end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next      # Step 5: Skip the target node

        return dummy.next               # Step 6: Return new head
