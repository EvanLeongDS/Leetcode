from collections import deque 
import math
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)] # adjacency list
        edge_weights = {} # for each edge track the weights

        # add graph to adjacency graph and edge weights 
        for time in times:
            adj[time[0]].append(time[1])

            if (time[0], time[1]) not in edge_weights:
                edge_weights[(time[0], time[1])] = time[2]
        
        dist = [math.inf for _ in range(n+1)]
        self.bfs(k, adj, edge_weights, dist)

        max_dist = 0
        for distance in dist[1:]:
            if distance == math.inf:
                return -1
            elif distance > max_dist:
                max_dist = distance
        
        return max_dist

    def bfs(self, k, adj, edge_weights, dist):
        queue = deque()
        dist[k] = 0 
        queue.append((k, 0))
        visited = set()
        min_weight = 0

        while queue:
            x, t = queue.popleft() 
            for node in adj[x]:
                weight = edge_weights[(x, node)]
                if t + weight < dist[node]:
                    dist[node] = t + weight
                    queue.append((node, t + weight))