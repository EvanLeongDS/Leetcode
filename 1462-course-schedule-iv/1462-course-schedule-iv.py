class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adjacency_list = [[] for _ in range(numCourses)]
        for [u, v] in prerequisites:
            adjacency_list[u].append(v)
        
        reach = [[False] * numCourses for _ in range(numCourses)]
        print(reach)
    
        # conduct dfs from each "starting" point
        for start in range(numCourses):
            to_visit = [start]
            while to_visit:
                node = to_visit.pop()
                for nxt in adjacency_list[node]:
                    if not reach[start][nxt]:
                        reach[start][nxt] = True
                        to_visit.append(nxt)
        
        answers = []
        for u, v in queries:
            result = reach[u][v]
            answers.append(result)
        return answers

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna