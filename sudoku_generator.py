import random
import sudoku_solver


class Sudoku:
    def __init__(self, n=3):
        self.n = n
        self.table = [[int(((i * n + i / n + j) % (n * n) + 1)) for j in range(n * n)] for i in range(n * n)]

    def __del__(self):
        pass

    def show(self):
        for i in range(self.n * self.n):
            print(self.table[i])


if __name__ == "__main__":
    sudoku = Sudoku()

    flook = [[0 for j in range(sudoku.n * sudoku.n)] for i in range(sudoku.n * sudoku.n)]
    iterator = 0
    difficult = sudoku.n ** 4

    while iterator < sudoku.n ** 4:
        i, j = random.randrange(0, sudoku.n * sudoku.n, 1), random.randrange(0, sudoku.n * sudoku.n, 1)
        if flook[i][j] == 0:
            iterator += 1
            flook[i][j] = 1

            temp = sudoku.table[i][j]
            sudoku.table[i][j] = 0
            difficult -= 1

            table_solution = []
            for copy_i in range(0, sudoku.n * sudoku.n):
                table_solution.append(sudoku.table[copy_i][:])

            i_solution = 0
            for solution in sudoku_solver.solve_sudoku((sudoku.n, sudoku.n), table_solution):
                i_solution += 1

            if i_solution != 1:
                sudoku.table[i][j] = temp
                difficult += 1
    sudoku.show()
    print("difficult = ", difficult)