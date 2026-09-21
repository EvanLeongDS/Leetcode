import math
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # find the max length in the words list
        # might not need this 
        min_len = math.inf
        for word in words:
            if len(word) < min_len:
                min_len = len(word)
        
        order_dict = {}
        # build a dictionary from the order 
        for index, char in enumerate(order):
            # iterate through each character 
            if char not in order_dict:
                order_dict[char] = index

        # iterate through the prefix 
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if order_dict[w1[j]] == order_dict[w2[j]]:
                    continue
                if order_dict[w1[j]] < order_dict[w2[j]]:
                    break
                return False
            else:
                if len(w1) > len(w2):
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna