#!/usr/bin/env python

class Cell:
    """
    represent a cell
    i for column
    j for row
    """
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.neigh = []
        self.free = True
        self.str = '[{},{}]'.format(j + 1, i + 1)

    def visit(self, route, depth):
        self.free = False
        route[depth] = self.str
        depth += 1
        if depth == len(route):
            print ('->'.join(route))
        else:
            for n in self.neigh:
                if n.free:
                    n.visit(route, depth)
        self.free = True

class Map:
    def __init__(self, n, m):
        """
        Init a map with n columns and m rows
        """
        self.map = [
                [Cell(i, j)
                    for i in range(n)
                    ] for j in range(m)
                ]

        self.route = [None for i in range(n*m)]

        for j in range(m):
            for i in range(n):
                c = self.map[j][i]

                for pi, pj in (
                        (-1, -1), ( 0, -1), ( 1, -1),
                        (-1,  0),           ( 1,  0),
                        (-1,  1), ( 0,  1), ( 1,  1)):
                    ni = i + pi
                    nj = j + pj

                    if 0 <= ni < n and 0 <= nj < m:
                        c.neigh.append(self.map[nj][ni])

    def visit(self, j, i):
        self.map[j][i].visit(self.route, 0)

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    m = n if len(sys.argv) < 3 else int(sys.argv[2])

    maxdepth = n * m

    themap = Map(n, m)

    #themap.visit(0 ,0)

    for j in range(m):
        for i in range(n):
            themap.visit(j, i)
