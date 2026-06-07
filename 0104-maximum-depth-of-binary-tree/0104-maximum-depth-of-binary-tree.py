# Definition for ab inary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self"""  """.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # basically do dfs 
        if not root:
            return 0 
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return 1 + max(depth_left, depth_right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna