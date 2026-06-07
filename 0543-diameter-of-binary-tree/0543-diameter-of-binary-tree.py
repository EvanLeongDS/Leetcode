# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        self.find_depth(root)
        return self.max_diameter
    def find_depth(self, node):
        if not node:
            return 0
        # find the max depth of the left side
        # find the max depth of the right side 
        left_depth = self.find_depth(node.left)
        right_depth = self.find_depth(node.right)
        self.max_diameter = max(self.max_diameter, left_depth+right_depth)
        return 1 + max(left_depth, right_depth)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna