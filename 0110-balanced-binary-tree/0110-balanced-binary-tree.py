# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recurse down left side and right side then see if the difference is never diff
        if not root:
            return True
        result = self.check_balance(root)
        if result == -1:
            return False
        else:
            return True

    def check_balance(self, node):
        if not node:
            return 0

        left_depth = self.check_balance(node.left)
        if left_depth == -1:
            return -1 
        right_depth = self.check_balance(node.right)
        if right_depth == -1:
            return -1 
        
        if abs(left_depth - right_depth) > 1: 
            return -1 
        return 1 + max(left_depth, right_depth)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna