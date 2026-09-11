# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB

        while currentA or currentB:
            if not currentA:
                currentA = headB
            elif not currentB:
                currentB = headA
            elif currentA == currentB:
                return currentA
            else:
                currentA = currentA.next
                currentB = currentB.next 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna