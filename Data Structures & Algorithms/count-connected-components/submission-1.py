class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set() # track which dfs nodes we hit
        count = 0 # each time we call dfs we increment the count by 1
        for node in range(n):
            if node not in visited:
                count += 1
                self.dfs(node, adj, visited)
        
        return count 

    def dfs(self, node, adj, visited):
        visited.add(node)
        for adj_node in adj[node]:
            if adj_node not in visited:
                self.dfs(adj_node, adj, visited)