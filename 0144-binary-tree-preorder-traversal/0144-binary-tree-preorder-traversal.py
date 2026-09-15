# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None, preorder_list = None) -> list[int]:
        if not root:
            return []
        if preorder_list is None:
            preorder_list = []

        # base case 
        if not root:
            return 
        preorder_list.append(root.val)
        # recurse the left tree or the right tree
        self.preorderTraversal(root.left, preorder_list)
        self.preorderTraversal(root.right, preorder_list)
        return preorder_list        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna