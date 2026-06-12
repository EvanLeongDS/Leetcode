# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_num = preorder[0]
        mid = None
        for index, num in enumerate(inorder):
            if num == root_num:
                mid = index
        left_preorder = preorder[1:mid+1]
        left_inorder = inorder[:mid]
        right_preorder = preorder[mid+1:]
        right_inorder = inorder[mid+1:]
        
        root = TreeNode(root_num)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna