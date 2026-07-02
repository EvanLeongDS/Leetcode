"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {}
        return self.dfs(node, visited)
        
    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        copy = Node(node.val)
        visited[node] = copy
        # iterate through the neighbors so the copy can get the exact same neighbors for its respective graph 
        for n in node.neighbors:
            copy_n = self.dfs(n, visited)
            copy.neighbors.append(copy_n)
    
        # return the copied adjacency list 
        return copy 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna