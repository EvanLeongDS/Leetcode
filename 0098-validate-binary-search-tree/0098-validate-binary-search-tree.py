# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        boolean = self.dfs(root, -math.inf, math.inf)
        if boolean == False:
            return False
        return True
    def dfs(self, node, min_range, max_range):
        # each node do the strictly less strictly more check
        if not node:
            return True
        if node.left:
            if node.left.val >= node.val:
                return False
        if node.right:
            if node.right.val <= node.val:
                return False
        if node.val >= max_range or node.val <= min_range:
            return False

        # traverse left side then # traverse right side 
        return self.dfs(node.left, min_range, node.val) and self.dfs(node.right, node.val, max_range)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna