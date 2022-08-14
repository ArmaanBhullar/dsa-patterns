class FastUnionFind:
    """
    Implements path compressed find and rank union
    """

    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x) -> int:
        """
        return root of node x and compress paths inbetween
        :param x:
        :return:
        """
        if x == self.root[x]:
            return x
        ls = []
        while x != self.root[x]:
            ls.append(x) # maintain path
            x = self.root[x]
        for node in ls:
            self.root[node] = x # compress path
        self.rank[x] = 1 # by this time, rank becomes 1
        return x

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else: # both are of same depth
                self.root[root_x] = root_y
                self.rank[root_y] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    uf = FastUnionFind(10)
    print(uf.connected(3, 5))
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(1, 5)
    uf.union(1, 2)
    uf.union(8, 9)
    uf.union(8, 7)
    print(uf.connected(3, 5))
    print(uf.connected(9, 7))
    print(uf.connected(1, 7))
    print(uf.root)
    print(uf.rank)
