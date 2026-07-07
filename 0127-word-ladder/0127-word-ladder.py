from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = set()
        return self.bfs(wordList, beginWord, endWord, visited)
    def bfs(self, wordList, beginWord, endWord, visited):
        visited.add(beginWord)
        queue = deque([(beginWord, 1)])
        wordSet = set(wordList)

        # iterate through all 26 letters
        while queue:
            current = queue.popleft()
            word, step = current
            if word == endWord:
                return step
            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    # if sliced word in the wordlist change it 
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, step + 1))
        
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna