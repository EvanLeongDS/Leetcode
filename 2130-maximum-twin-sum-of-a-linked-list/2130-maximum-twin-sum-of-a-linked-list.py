# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0 

        # use slow fast method to reverse second half of the list
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # perform reversal function from slow onward
        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt 
        
        current_left = head 
        current_right = prev

        while current_left and current_right:
            left_val = current_left.val
            right_val = current_right.val
            twin_sum = left_val + right_val
            max_sum = max(max_sum, twin_sum)

            current_left = current_left.next
            current_right = current_right.next
        
        return max_sum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna