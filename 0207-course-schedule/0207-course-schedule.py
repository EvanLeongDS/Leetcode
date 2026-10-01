class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if you detect a cycle it is false

        # create the adjacency list  
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites: # take bi before ai 
            adj[b].append(a)
        
        # 0 is unvisited 1 is visiting 2 is done
        state = [0 for _ in range(numCourses)]

        for i in range(numCourses):
            if not self.dfs(i, state, adj):
                return False
        return True 

    def dfs(self, course, state, adj):
        state[course] = 1
        for adj_course in adj[course]:
            if state[adj_course] == 1:
                    return False
            elif state[adj_course] == 0:
                if not self.dfs(adj_course, state, adj):
                    return False
        state[course] = 2
        return True


