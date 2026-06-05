class ListNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # dictionary for mapping 

        # establish dummy nodes
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        # establish next
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # it is used therefore move it to front
            self.remove(node)
            self.insert_at_head(node)

            return node.value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:

        # update values
        if key in self.cache:
            # update the value of the keys
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_at_head(node)
        else:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            # update the linked list
            self.insert_at_head(new_node)
        # evict key
        if len(self.cache) > self.capacity:
            node_to_evict = self.tail.prev
            # manipulate pointers
            self.remove(node_to_evict)
            del self.cache[node_to_evict.key]

    def remove(self, node):
        # Take the next left node and the next right node and link them together
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert_at_head(self, node):
        # insert a new node at the front of the linked list 
        current_head = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = current_head
        current_head.prev = node
    
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna