# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot) == True:
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, node, subnode):
        # we've reached a subroot, check if the trees are equal
        if not node and not subnode:
            return True
        if not node or not subnode:
            return False
        if node.val != subnode.val:
            return False  
        left_side = self.isSameTree(node.left, subnode.left)
        right_side = self.isSameTree(node.right, subnode.right)

        if left_side and right_side:
            return True
        else:
            return False



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna