"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None} # We don't need to handle null cases separately

        # First pass: create a copy of each node and store it in the dictionary
        curr = head
        while curr:
            copy = Node(curr.val) # Create a copy with the same value
            oldToCopy[curr] = copy # Map original node -> new node
            curr = curr.next # Move to next node
        # Second pass: assign next and random pointer to each copy node
        curr = head
        while curr:
            copy = oldToCopy[curr] # Get the copy node
            copy.next = oldToCopy[curr.next] # Set the next node
            copy.random = oldToCopy[curr.random] # Set the random node
            curr = curr.next # Move to next node
 
        return oldToCopy[head] # Return the copied head node
