# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.dfs(root)
        return self.stack[k-1]
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.stack.append(node.val)
        self.dfs(node.right)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna