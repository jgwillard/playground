class UnionFind(object):
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.count = size
        self.weight = [1] * size

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        # path compression: if the examined node is not a root, set its
        # parent to be the root so that future lookups take O(1) time
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.weight[i] < self.weight[j]:
            self.root[i] = j
            self.weight[j] += self.weight[i]
        else:
            self.root[j] = i
            self.weight[i] += self.weight[j]

        self.count -= 1

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)
