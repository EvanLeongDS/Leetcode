from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: n-1 edges and no cycles and every node is connected

        # check connectivity: n nodes and n -1 edges
        edge_count = len(edges)
        if n != edge_count + 1:
            return False
        if n == 1 and edge_count == 0:
            return True
        # check for cycles 
        start = edges[0][0]
        if self.bfs(edges, n, start) == False:
            return False
        return True 
    def bfs(self, edges, n, start):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {start}
        queue = deque([(start , 0, -1)]) #node, distance

        while queue:
            node, distance, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == parent:
                    # no reason to do bfs back to the parent in the unidrected graph
                    pass
                elif neighbor in visited and neighbor != parent:
                    return False 
                else:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1, node))
        # check if we actually got to every node
        if len(visited) != n:
            return False
        return True
    