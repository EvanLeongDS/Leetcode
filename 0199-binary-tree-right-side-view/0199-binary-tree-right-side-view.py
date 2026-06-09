# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base case if nothing return empty list 
        if not root:
            return [] 
        self.dfs(root, 0)
        # conduct dfs helper while tracking depth
        return self.result 

    def dfs(self, node, depth):
        # conduct dfs and increase the depth count by 1 
        if not node:
            return
        if depth == len(self.result):
            self.result.append(node.val)
        
        # conduct dfs starting right first 
        self.dfs(node.right, depth+1)
        self.dfs(node.left, depth+1)
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna