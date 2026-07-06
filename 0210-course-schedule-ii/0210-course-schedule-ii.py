class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order_list = [] # final thing to return 

        state = [0] * numCourses # node state tracker
        graph = [[] for _ in range(numCourses)] # turn prerequisites into an adjacency list
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        for node in range(numCourses):
            if state[node] == 0:
                if not self.dfs(graph, state, node, order_list):
                    return []

        # reverse order_list according to topological sort
        order_list = order_list[::-1]
        return order_list

    def dfs(self, graph, state, node, order_list):
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True
        if state[node] == 0:
            # we have reached this node, mark it as 1 
            state[node] = 1
            for neighbor in graph[node]:
                if not self.dfs(graph, state, neighbor, order_list):
                    return False
            state[node] = 2
            order_list.append(node)
            # indicate that there is no cycles here
            return True
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna