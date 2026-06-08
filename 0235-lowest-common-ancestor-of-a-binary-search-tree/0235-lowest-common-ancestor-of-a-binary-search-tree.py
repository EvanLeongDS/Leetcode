# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        while current is not None: 
            # move right if both are greater
            if p.val > current.val and q.val > current.val:
                current = current.right
            # move to left of current if both are less 
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # we either have a split or one is included
                # therefore return current 
                return current
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna