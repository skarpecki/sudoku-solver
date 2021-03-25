from copy import deepcopy

def create_sudoku():
    sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]
    return sudoku

def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0:
            print()
        for j in range(len(sudoku)):
            if j % 3 == 0:
                print("| ", end="")
            print("{} ".format(sudoku[i][j]), end="")
        print("|")
    print()

def _validate_column(sudoku, num, col_no):
    for i in range(len(sudoku)):
        if num == sudoku[i][col_no]:
            return False
    return True

def _validate_row(sudoku, num, row_no):
    for i in range(len(sudoku)):
        if num == sudoku[row_no][i]:
            return False
    return True

def _validate_part(sudoku, num, row_no, col_no):
    row_start = int(row_no/3) * 3
    col_start = int(col_no/3) * 3
    for i in range(3):
        for j in range(3):
            if num == sudoku[row_start + i][col_start + j]:
                return False
    return True

def validate_num(sudoku, num, row_no, col_no):
    return \
        _validate_column(sudoku, num, col_no) and \
        _validate_row(sudoku, num, row_no) and \
        _validate_part(sudoku, num, row_no, col_no)

def find_next_empty(sudoku, row_start, col_start):
    mul = 1
    for i in range(row_start, len(sudoku)):
        for j in range(col_start * mul, len(sudoku)):
            if sudoku[i][j] == 0:
                return (i, j)
        mul = 0
    return(-1, -1)

def solve(sudoku, row_start=0, col_start=0):
    row_no, col_no = find_next_empty(sudoku, row_start, col_start)
    for i in range(1,10):
        temp_sudoku = deepcopy(sudoku)
        if validate_num(sudoku, i, row_no, col_no):
            temp_sudoku[row_no][col_no] = i
            (row_idx, col_idx) = find_next_empty(temp_sudoku, row_no, col_no)
            if (row_idx, col_idx) == (-1, -1):
                return temp_sudoku
            temp_sudoku = solve(temp_sudoku, row_idx, col_idx)
            if temp_sudoku is not None:
                return temp_sudoku 
    return None


if __name__ == "__main__":
    sudoku = create_sudoku()
    print_sudoku(sudoku)
    # print(_validate_column(sudoku, 8, 0))
    # print(_validate_row(sudoku, 9, 5))
    # print(validate_num(sudoku, 8, 3, 5))
    # print(find_next_empty(sudoku, 8, 6))
    print_sudoku(solve(sudoku))