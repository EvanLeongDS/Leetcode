from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        start = '0000'
        return self.bfs(deadends, start, target)

    def bfs(self, deadends, start, target):
        seen = set(deadends)                          # 1. what should count as "blocked" from the start?
        if start in seen:
            return -1                           # 2. stuck before turning

        queue = deque()
        seen.add(start)
        queue.append((start, 0))                 # combo, turns

        while queue:
            combo, turn = queue.popleft()

            if combo == target:                       # 3. is the WHOLE lock open?
                return turn                       # 4. how many turns did it take?

            for index in range(4):               # each wheel
                for move in [1, -1]:             # up and down
                    new_combo = combo[:index] + str((int(combo[index]) + move) % 10) + combo[index+1:]   # 5.
                    if new_combo not in seen:     # 6. skip deadends and repeats
                        seen.add(new_combo)            # 7.
                        queue.append((new_combo, turn + 1)) # 8. new combo, one more turn

        return -1                              # 9. queue empty, never opened