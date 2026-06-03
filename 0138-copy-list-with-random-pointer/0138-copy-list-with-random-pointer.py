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
        pointer_dict = {}
        if head is None:
            return None
        current = head
        # first pass establish that everything exists
        while current is not None:
            if current not in pointer_dict:
                pointer_dict[current] = Node(current.val)
            # move it forward
            current = current.next

        # second pass add all arrows
        for original in pointer_dict:
            copy = pointer_dict[original]
            if original.next is not None:
                copy.next = pointer_dict[original.next]
            else:
                copy.next = None
            if original.random is not None:
                copy.random = pointer_dict[original.random]
            else:
                copy.random = None

    
        return pointer_dict[head]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna