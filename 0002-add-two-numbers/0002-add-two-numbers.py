# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # set up multiplier plus sum 
        l1_sum = 0
        l1_multiplier = 1 
        while l1:
            node_number = l1.val
            l1_sum += node_number * l1_multiplier
            l1_multiplier = l1_multiplier * 10
            l1 = l1.next

        l2_sum = 0
        l2_multiplier = 1 
        while l2:
            node_number = l2.val
            l2_sum += node_number * l2_multiplier
            l2_multiplier = l2_multiplier * 10
            l2 = l2.next

        # build the new linked list 
        big_sum = l1_sum + l2_sum
        dummy = ListNode(0)
        curr = dummy

        if big_sum == 0: 
            curr.next = ListNode(0) 
            return dummy.next
        while big_sum > 0:
            list_num = big_sum % 10
            curr.next = ListNode(list_num)
            big_sum = big_sum // 10
            curr = curr.next
        return dummy.next 



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna