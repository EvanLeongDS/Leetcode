# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good_node_list = []
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0 
        self.dfs(root, root.val)
        return len(self.good_node_list)

    def dfs(self, node, max_so_far):
        if not node:
            return
        if node.val >= max_so_far:
            self.good_node_list.append(node.val)
            max_so_far = node.val
        self.dfs(node.left, max_so_far)
        self.dfs(node.right, max_so_far)
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna