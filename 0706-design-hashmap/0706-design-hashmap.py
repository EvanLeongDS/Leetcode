class MyHashMap:

    def __init__(self):
        self.hash_map = []

    def put(self, key: int, value: int) -> None:
        key_found = False
        for index, pair in enumerate(self.hash_map):
            if pair[0] == key:
                key_found = True
                self.hash_map[index][1] = value
        if not key_found:
            self.hash_map.append([key, value])
        
    def get(self, key: int) -> int:
        # see if we can get the value of the key otherwise return -1 
        key_found = False
        for pair in self.hash_map:
            if pair[0] == key:
                key_found = True
                return pair[1]
        if not key_found:
            return -1 

    def remove(self, key: int) -> None:
        for pair in self.hash_map:
            if pair[0] == key:
                self.hash_map.remove(pair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna