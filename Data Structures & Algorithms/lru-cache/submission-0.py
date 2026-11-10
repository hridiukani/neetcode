class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)   # remove...
        self.cache[key] = val       # ...and reinsert, so it moves to the end (most recent)
        return val

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            oldest = next(iter(self.cache))   # first key = least recently used
            del self.cache[oldest]