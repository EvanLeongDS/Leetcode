# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # have two pointers: a slow node and a fast node that shows the gap 
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # move the fast pointer n times to create the gap
        for _ in range(n):
            fast = fast.next

        # advance slow and fast up to the point where we need to cut off the node 
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        # remove the nth node
        slow.next = slow.next.next
        return dummy.next

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna