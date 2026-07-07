class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # overall strategy: conduct dfs until you find a cycle then remove the answer that occurs last in the input 
        n = len(edges)
        parent = list(range(n + 1)) 
        
        for x, y in edges:
            if self.union(x, y, parent) == False:
                return [x, y]

        
    def find(self, x, parent):
        # returns the representative (group leader) of x's connected component
        # climbs parent pointers until it reaches a node that points to itself
        while parent[x] != x:
            x = parent[x]
        return x
            

    def union(self, x, y, parent):
        # merges x's group and y's group into one
        # returns False if they were already in the same group (this edge is redundant)
        # returns True if they were merged successfully
        root_x = self.find(x, parent)
        root_y = self.find(y, parent)
        if root_x == root_y:
            return False
        else:
            parent[root_x] = root_y
            return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna