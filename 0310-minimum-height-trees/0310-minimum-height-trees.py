from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if not edges:
            return [0]
            
        min_height_list = [] # thing i will return in the end 
        # create adjacency list 
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        degree = [len(neighbors) for neighbors in adj]

        # add all adjacency nodes with length(1)
        queue = deque()
        for index, node in enumerate(adj):
            # we want length 1 
            if len(node) == 1:
                queue.append(index)
        
        self.bfs(queue, adj, degree, n)
        return list(queue)
        
    def bfs(self, queue, adj, degree, n):
        remaining = n 
        while remaining > 2:
            leaves_remaining = len(queue)
            for _ in range(leaves_remaining):
                leaf = queue.popleft()
                remaining -= 1
                for node in adj[leaf]:
                    degree[node] -= 1
                    if degree[node] == 1:
                        queue.append(node)