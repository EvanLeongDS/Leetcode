class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycles via dfs
        graph = [[] for _ in range(numCourses)]

        # establish a dictionary
        state = [0] * numCourses # 0 is unvisited 1 is in progress 2 is done 

        # establish graph as an adjacency list
        for dest, src in prerequisites:
            graph[src].append(dest)

        # loop through everything return true if no cycles false if you can't
        for node in range(numCourses):
            if state[node] == 0:
                if not self.dfs(graph, state, node):
                    return False
        return True

    def dfs(self, graph, state, node):
        # run dfs on all nodes to test for cycles
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True
        if state[node] == 0:
            state[node] = 1
            # call dfs on the neighbors
            for neighbor in graph[node]:
                if not self.dfs(graph, state, neighbor):
                    return False
            state[node] = 2

        # no cycles here, therefore return true
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna