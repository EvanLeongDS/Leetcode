class TimeMap:

    def __init__(self):
        self.store = {} # dictionary for timestamps

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        # find the value either bar or bar2 via binary search
        if key not in self.store:
            return ""
        timeline = self.store[key]
        
        # check if you timestamp is greater than timeline 
        if timestamp < timeline[0][0]:
            return ""

        # conduct binary search
        low = 0 
        high = len(timeline) - 1 
        while low <= high:
            mid = (low + high) // 2 
            mid_timestamp = timeline[mid][0]

            if mid_timestamp == timestamp:
                return timeline[mid][1]
            elif timestamp > mid_timestamp:
                # search right side 
                res = timeline[mid][1]
                low = mid + 1
            else:
                high = mid - 1 
        # if its not exactly equal once the loop ends we know it was behind
        return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna