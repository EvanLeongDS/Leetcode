class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if you can reach every node its possible 
        cycle_tracker = [0] * n
        # 0 is unseen 1 is seen 2 is cycle

        # create adjacency list for an undirected graph 
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # check for connectivity
        if len(edges) + 1 != n:
            return False

        # conduct dfs from each node 
        self.dfs(0, adj, cycle_tracker)                 # CHANGED: dfs once from 0
        for index in range(len(adj)):
            if cycle_tracker[index] == 0:               # CHANGED: anyone unreached?
                return False
        return True

    def dfs(self, node, adj, cycle_tracker):
        # conduct dfs to make sure the nodes go through and we dont get no cycles
        cycle_tracker[node] = 1 
        for adj_node in adj[node]:
            if cycle_tracker[adj_node] == 1:
                continue
            elif cycle_tracker[adj_node] == 0:
                if not self.dfs(adj_node, adj, cycle_tracker):
                    return False
        return True