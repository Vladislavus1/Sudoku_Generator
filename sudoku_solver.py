from itertools import product


def solve_sudoku(size, grid):
    r, c = size
    n = r * r
    x = ([("rc", rc) for rc in product(range(n), range(n))] +
         [("rn", rn) for rn in product(range(n), range(1, n + 1))] +
         [("cn", cn) for cn in product(range(n), range(1, n + 1))] +
         [("bn", bn) for bn in product(range(n), range(1, n + 1))])
    y = dict()
    for r1, c1, n1 in product(range(n), range(n), range(1, n + 1)):
        b = (r1 // r) * r + (c1 // c)
        y[(r1, c1, n1)] = [
            ("rc", (r1, c1)),
            ("rn", (r1, n1)),
            ("cn", (c1, n1)),
            ("bn", (b, n1))]
    x, y = exact_cover(x, y)
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n:
                select(x, y, (i, j, n))
    for solution in solve(x, y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid


def exact_cover(x, y):
    x = {j: set() for j in x}
    for i, row in y.items():
        for j in row:
            x[j].add(i)
    return x, y


def solve(x, y, solution):
    if not x:
        yield list(solution)
    else:
        c = min(x, key=lambda c_arg: len(x[c_arg]))
        for r in list(x[c]):
            solution.append(r)
            cols = select(x, y, r)
            for s in solve(x, y, solution):
                yield s
            deselect(x, y, r, cols)
            solution.pop()


def select(x, y, r):
    cols = []
    for j in y[r]:
        for i in x[j]:
            for k in y[i]:
                if k != j:
                    x[k].remove(i)
        cols.append(x.pop(j))
    return cols


def deselect(x, y, r, cols):
    for j in reversed(y[r]):
        x[j] = cols.pop()
        for i in x[j]:
            for k in y[i]:
                if k != j:
                    x[k].add(i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()