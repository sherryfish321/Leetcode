class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:   # Ensure fast can move 2 steps
            slow = slow.next        # Move slow by 1 step
            fast = fast.next.next   # Move fast by 2 steps
            if slow == fast:        # Same node → cycle detected
                return True
        return False                 # fast reached end → no cycle
