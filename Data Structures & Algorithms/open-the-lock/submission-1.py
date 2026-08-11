from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # base case 
        if target == "0000":
            return 0 
        visited = set(deadends)
        if "0000" in visited:
            return -1
        queue = deque([("0000", 0)]) # state, number of turns
    
        visited.add("0000")
        return self.bfs(queue, visited, target)
    def bfs(self, queue, visited, target):
        # conduct bfs, figure out the number of turns 
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            
            # conduct bfs through each digit
            for i in range(4):
                digit = int(state[i])
                # try both directions
                for change in [1, -1]:
                    new_digit = (digit + change) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    if new_state in visited:
                        pass
                    elif new_state != target:
                        visited.add(new_state)
                        queue.append((new_state, turns+1))
                    else:
                        return turns + 1 
        return -1