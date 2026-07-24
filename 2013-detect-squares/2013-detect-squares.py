import math
class DetectSquares:

    def __init__(self):
        self.dict = {}

    def add(self, point: List[int]) -> None:
        # add new points from the stream to the data structure 
        p = tuple(point)
        if p not in self.dict:
            self.dict[p] = 1
        else:
            self.dict[p] += 1

    def count(self, point: List[int]) -> int:
        count = 0 
        for key, value in self.dict.items():
            dx = point[0] - key[0]
            dy = point[1] - key[1]
            if abs(dx) == abs(dy) and abs(dx) > 0 and abs(dy) > 0:
                if (point[0], key[1]) in self.dict and (key[0], point[1]) in self.dict:
                    count += (value * self.dict[(point[0], key[1])] * self.dict[(key[0], point[1])])
        return count 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna