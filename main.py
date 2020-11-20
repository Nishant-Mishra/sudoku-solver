
from typing import List, Tuple, Union

# Assuming input as a 2D list vector of 9x9
# 0 => empty
sample_board = [
    [0, 2, 9, 0, 8, 0, 5, 0, 0],
    [1, 0, 0, 0, 5, 0, 0, 0, 2],
    [0, 0, 5, 6, 0, 2, 0, 1, 0],
    [9, 0, 0, 8, 0, 0, 2, 0, 5],
    [0, 0, 8, 0, 0, 7, 0, 6, 0],
    [0, 5, 0, 0, 2, 0, 0, 7, 0],
    [8, 0, 0, 4, 0, 0, 6, 0, 0],
    [0, 0, 2, 0, 1, 0, 0, 0, 3],
    [5, 0, 0, 2, 0, 3, 8, 0, 7]
]


def solve1(board: List[List[int]]):

    stack = []
    k = 1
    found = False
    pos = get_empty(board)
    steps = 0
    while pos is not None:
        steps += 1
        for n in range(k, len(board) + 1):
            if check_valid(board, pos, n):
                found = True
                board[pos[0]][pos[1]] = n
                stack.append((pos, n + 1))
                break
            else:
                found = False

        try:
            if not found:
                pos, k = stack.pop()
                board[pos[0]][pos[1]] = 0
            else:
                k = 1
                pos = get_empty(board)
        except IndexError:
            print("There is no Solution to this Sudoku")
            return

    print("Solved in {:04d} steps".format(steps))


def solve2(board: List[List[int]]):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for n in range(len(board) + 1):
                    if check_valid(board, (i, j), n):
                        board[i][j] = n
                        solve2(board)
                        board[i][j] = 0
                return
    print_board(board)


def check_valid(board: List[List[int]], pos: Tuple[int, int], num: int) -> bool:

    # Basic Boundary Checks
    if num < 1 or num > len(board) or \
       pos[0] < 0 or pos[0] >= len(board) or \
       pos[1] < 0 or pos[1] >= len(board[0]):
        return False

    # Check Row
    for j in range(len(board[0])):
        if board[pos[0]][j] == num and j != pos[1]:
            return False

    # Check Col
    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False

    # Check Box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for i in range(box_row * 3, (box_row + 1) * 3):
        for j in range(box_col * 3, (box_col + 1) * 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def get_empty(board: List[List[int]]) -> Union[Tuple[int, int], None]:
    for row_id, row in enumerate(board):
        for col_id, num in enumerate(row):
            if num == 0:
                return row_id, col_id

    return None


def print_board(board: List[List[int]]):
    print("")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 13)
        print(" ", end=" ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print("")
    print("")


def main():
    board = sample_board
    print_board(board)
    solve2(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not check_valid(board, (i, j), board[i][j]):
                print("Wrong: sample_board{}={}".format((i, j), board[i][j]))
    print_board(board)


if __name__ == '__main__':
    main()

