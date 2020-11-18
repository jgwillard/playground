from typing import Dict, List


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table: Dict[int, int] = {}
        self.queue: List[int] = []

    def get(self, key: int) -> int:
        val = self.table.get(key)
        if val is None:
            return -1
        if key in self.table:
            self.queue.remove(key)
        if len(self.queue) == self.capacity:
            self.queue.pop(0)
        self.queue.append(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.queue.remove(key)
        if len(self.queue) == self.capacity:
            evicted = self.queue.pop(0)
            self.table.pop(evicted)
        self.queue.append(key)
        self.table[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
