# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None, postorder_list = None) -> list[int]:
        if not root:
            return [] 
        if postorder_list is None:
            postorder_list = []
        
        # base case
        if not root:
            return 
        # recurse 
        self.postorderTraversal(root.left, postorder_list)
        self.postorderTraversal(root.right, postorder_list)
        postorder_list.append(root.val)

        # return final product
        return postorder_list

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna