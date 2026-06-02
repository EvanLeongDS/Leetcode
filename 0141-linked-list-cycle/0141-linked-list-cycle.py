# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # will go one step at a time
        fast = head # will go two steps at a time 

        # let them meet twice while fast and fast.next is not None
        while fast and fast.next is not None:
            # slow increments once fast increments twice
            slow = slow.next
            fast = fast.next.next

            # check if slow == fast
            if slow == fast:
                return True
        return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna