# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        result = []
        queue = deque([root])
        print(queue)
        while queue:
            # Take a snapshot of how many nodes are currently in the queue
            # Create an empty list just for this level's numbers 
            level_size = len(queue)
            current_level_values = []

            # Run a loop EXACTLY that many times (based on your snapshot size):
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Append your current_level_values list to your master result list.
            result.append(current_level_values)
        return result 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna