sudoku_grid = []
def main():
    global sudoku_grid
    n = int(input())
    while n:
        for i in range(9):
            sudoku_grid.append(list(map(int, input().split(' '))))
        solve_sudoku()
        print_sudoku()
        # reset sudoku grid
        sudoku_grid = []
        n -= 1
    return


def print_sudoku():
    for row in sudoku_grid:
        for val in row:
            print("{0} ".format(val), end='')
        print()


def solve_sudoku():
    global sudoku_grid
    row, col = find_empty_cell()
    if (row, col) == (-1, -1):
        return True

    for i in range(1, 10):
        if check_constraint(i, row, col):
            sudoku_grid[row][col] = i
            if solve_sudoku():
                return sudoku_grid
            sudoku_grid[row][col] = 0
    return False


def check_constraint(digit, row, col):
    if row_constraint(digit, row) and column_constraint(digit, col) and box_constraint(digit, row, col):
        return True
    return False

def row_constraint(digit, row):
    if digit in sudoku_grid[row]:
        return False
    return True

def column_constraint(digit, col):
    for row_content in sudoku_grid:
        if digit == row_content[col]:
            return False
    return True

def box_constraint(digit, row, col):
    box_starting_row = row - (row % 3)
    box_starting_col = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if digit == sudoku_grid[box_starting_row + i][box_starting_col + j]:
                return False
    return True

def find_empty_cell():
    for idx, row in enumerate(sudoku_grid):
        if 0 in row:
            return idx, row.index(0)
    return -1, -1


if __name__ == '__main__':
    main()
