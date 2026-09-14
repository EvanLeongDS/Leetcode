# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], inorder_list=None) -> List[int]:
        if not root:
            return []
        if inorder_list is None:
            inorder_list = []

        node = root 
        if not node:
            return 
        
        self.inorderTraversal(node.left, inorder_list)
        inorder_list.append(node.val)
        self.inorderTraversal(node.right, inorder_list)

        return inorder_list

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna